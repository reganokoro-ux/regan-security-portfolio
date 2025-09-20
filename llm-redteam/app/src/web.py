from flask import Flask, request, jsonify, render_template_string
from app.src.llm_integration import summarize_profile
import uuid

# Create Flask app — note the double underscores around __name__
app = Flask(__name__)

# In-memory "database" for MVP
USERS = {}
# Each user has: { "bio": "...", "page_secret": "..." }

@app.route("/")
def index():
    return """
    <h2>LLM-RedTeam MVP</h2>
    <p>POST /profile to store a bio. GET /admin/summary?user_id=... to request LLM summary (vulnerable).</p>
    """

@app.route("/profile", methods=["POST"])
def profile():
    """
    POST JSON: {"user_id": "optional", "bio": "text"}
    Returns user_id created/updated.
    """
    data = request.get_json() or {}
    bio = data.get("bio", "")
    user_id = data.get("user_id") or str(uuid.uuid4())
    # page_secret simulates a per-page / per-user secret the LLM must NOT leak.
    page_secret = USERS.get(user_id, {}).get("page_secret") or str(uuid.uuid4())
    USERS[user_id] = {"bio": bio, "page_secret": page_secret}
    return jsonify({"user_id": user_id, "bio": bio, "page_secret_hint": "hidden"}), 201

@app.route("/profile/view")
def view_profile():
    """Simple view for manual inspection (HTML)"""
    user_id = request.args.get("user_id")
    if not user_id or user_id not in USERS:
        return "No such user. Use /profile to create.", 404
    bio = USERS[user_id]["bio"]
    # intentionally render unsanitized bio (vulnerable XSS-like demo)
    html = f"""
    <h3>User profile</h3>
    <div id="bio">{bio}</div>
    <p>User ID: {user_id}</p>
    """
    # render_template_string used for simplicity
    return render_template_string(html)

@app.route("/admin/summary", methods=["GET"])
def admin_summary():
    """
    Admin endpoint that calls the LLM to summarize the user's bio.
    This function intentionally passes both the bio and the page_secret to the LLM,
    simulating a case where LLM has access to sensitive context and might leak it
    if tricked by prompt-injection contained in the bio.
    """
    user_id = request.args.get("user_id")
    if not user_id or user_id not in USERS:
        return jsonify({"error": "user_id missing or not found"}), 404

    record = USERS[user_id]
    bio = record["bio"]
    page_secret = record["page_secret"]

    llm_reply = summarize_profile(bio=bio, page_secret=page_secret)

    # Intentionally render LLM reply unsafely (vulnerable flow)
    html = f"""
    <h3>Admin Summary</h3>
    <div id="llm_reply">{llm_reply}</div>
    <p>User ID: {user_id}</p>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
