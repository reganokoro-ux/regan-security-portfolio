FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY app /app/app
COPY tooling /app/tooling

ENV FLASK_APP=app.src.web
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8000
ENV PYTHONPATH=/app

EXPOSE 8000

CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
