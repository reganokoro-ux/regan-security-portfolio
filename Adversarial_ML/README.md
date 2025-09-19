# Adversarial Spam Testing Demo

## Description
Python script demonstrating adversarial testing on a text classifier. Shows how small changes in spam messages can affect the predictions of an automated spam filter. This simulates a *real-life challenge* in cybersecurity and NLP systems.

## Tools Used
- Python
- Hugging Face Transformers
- Adversarial input testing

## How to Run On VMs
1. cd ~/Desktop/regan-security-portfolio/Adversarial_ML

2. Create a Python virtual environment 
python3 -m venv venv

3. Activate the virtual environment:
source venv/bin/activate

4. Install dependencies:
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install transformers

5. Run the script:
python3 adversarial_spam_demo.py

## How to Run on Colab
1. Upload adversarial_spam_demo.py to a new Colab notebook.
2. Install dependencies: 
   !pip install torch --index-url https://download.pytorch.org/whl/cpu
   !pip install transformers
3. Run the script: 
   !python3 adversarial_spam_demo.py

## Learning Outcomes
- Understanding adversarial inputs in NLP.
- Testing model robustness against evasion attempts.
- Demonstrates practical cybersecurity and ML sk
