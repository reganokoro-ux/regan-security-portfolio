# LLM RedTeam

## Project Overview
The **LLM RedTeam** project focuses on evaluating and testing Large Language Model (LLM) systems for potential vulnerabilities. It demonstrates practical security testing techniques, highlighting potential risks such as data leakage and exposure of sensitive information. The project includes proof-of-concept (PoC) scenarios with safe, redacted examples.

---

## Screenshots
Here are examples of PoC results captured during testing:

![PoC Secret Leak 1](llm-redteam/docs/screenshots/poc_secret_leak_redacted.png)  
*Figure 1: Example of secret data exposure (redacted).*

![PoC Secret Leak 2](llm-redteam/docs/screenshots/poc_secret_leak_redacted_2.png)  
*Figure 2: Another PoC highlighting sensitive information leak (redacted).*

---

## Features
- Detection of sensitive data leakage from LLM responses.
- Safe, reproducible PoC scripts demonstrating vulnerabilities.
- Documentation of testing methodology and security findings.
- Step-by-step instructions for reproducing tests in a controlled environment.

---

## Installation & Setup
1.Make sure Docker and Docker Compose v2 are installed on your system.
2. Clone the repository:
```bash

git clone https://github.com/reganokoro-ux/regan-security-portfolio.git
cd regan-security-portfolio/llm-redteam


----
3. Run docker compose up --build
4 on another shell paste git clone https://github.com/reganokoro-ux/regan-security-portfolio.git
cd regan-security-portfolio/llm-redteam
5 Run python3 tooling/xss_poc.py
