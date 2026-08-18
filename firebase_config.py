"""
firebase_config.py

Initializes the Firebase Admin SDK using a local service-account key file
and exposes a Firestore client (`db`) for the rest of the app to use.

Local development only:
- firebase-key.json must sit next to this file.
- Never commit firebase-key.json to version control.
- Never send its contents to the frontend or to Gemini.
"""
import os
import firebase_admin
from firebase_admin import credentials

# Current file irukura exact folder path-a edukkum
base_dir = os.path.dirname(os.path.abspath(__file__))
key_path = os.path.join(base_dir, "firebase-key.json")

# Debugging logs (Render console la path check panna)
print("====================================")
print(f"Current Directory: {base_dir}")
print(f"Searching key at: {key_path}")
print(f"Files inside folder: {os.listdir(base_dir)}")
print("====================================")

if not firebase_admin._apps:
    if os.path.exists(key_path):
        cred = credentials.Certificate(key_path)
        firebase_admin.initialize_app(cred)
    else:
        raise FileNotFoundError(f"Key file not found at path: {key_path}")
