# LLM-RedTeam — MVP

*Research-only* intentionally vulnerable demo showing chained AppSec + LLM prompt-injection (XSS → LLM exfil).

Quick demo (MVP):
1. Build & run: docker-compose up --build
2. In a new terminal run: python tooling/xss_poc.py
3. Observe PoC output: it will print whether the "secret" was exfiltrated.

WARNING: this repo intentionally includes insecure code for research/education. Do NOT run against external services. Responsible disclosure & ethics apply.

Contents:
- app/ — Flask app and mock LLM integration
- tooling/ — exploit PoC scripts
- Dockerfile, docker-compose.yml — for local runs
