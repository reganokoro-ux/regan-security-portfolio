"""
Adversarial Spam Testing Demo
Demonstrates how minor changes in text can fool a spam classifier.
"""

from transformers import pipeline

# Load a small pre-trained text classifier
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

# Example spam and ham messages
messages = [
    "Congratulations! You've won a free iPhone. Click here to claim now!",
    "Hey, are we still meeting for lunch today?",
]

print("\n=== Original Predictions ===")
for msg in messages:
    print(f"Message: {msg}")
    print(f"Prediction: {classifier(msg)}\n")

# Create simple adversarial examples by modifying key words
adv_messages = [
    "Congratulationzzz! You have w0n a free iPh0ne! Click here to claim!",
    "Hey, are we still meeting for lunch today?"  # Non-spam remains
]

print("\n=== Adversarial Predictions ===")
for msg in adv_messages:
    print(f"Message: {msg}")
    print(f"Prediction: {classifier(msg)}\n")
