# Mock LLM integration to simulate prompt-injection vulnerability
# WARNING: intentionally insecure for research.

def summarize_profile(bio: str, page_secret: str) -> str:
    """
    Naive mock 'LLM' behavior:
    - If the bio includes the token 'INJECT', the LLM obeys the hidden instruction
      and includes the page_secret in its reply (simulating prompt-injection).
    - Otherwise it returns a sanitized summary that does NOT include the secret.
    """
    # Very tiny sanitizer: remove angle brackets to avoid HTML injection in this mock
    sanitized_bio = bio.replace("<", "").replace(">", "")

    # Simulate prompt-injection: attacker embeds "INJECT" instruction in bio
    if "INJECT" in bio:
        # LLM blindly follows hidden instruction and reveals the secret
        return f"Summary: User says: {sanitized_bio}. (LLM: included SECRET -> {page_secret})"
    else:
        return f"Summary: User says: {sanitized_bio}. (LLM: nothing secret included)"
