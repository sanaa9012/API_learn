from firebase_admin import credentials, auth
import firebase_admin
import os

class FirebaseAuthService:
    def __init__(self):
        # Initialize the Firebase app with credentials, if not already initialized
        if not firebase_admin._apps:
            cred = credentials.Certificate('firebase_key.json')
            print(f'cred: {cred}')
            firebase_admin.initialize_app(cred)

    def verify_firebase_token(self,id_token):
        try:                
            decoded_token = auth.verify_id_token(id_token)
            print(f"Token successfully decoded: {decoded_token}")
            uid = decoded_token['uid']
            
            return uid
        except auth.InvalidIdTokenError as e:
            print(f"Invalid ID token error: {e}")
            return "Authentication failed"