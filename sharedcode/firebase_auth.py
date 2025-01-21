from firebase_admin import credentials, auth
import firebase_admin
import os

class FirebaseAuthService:
    def __init__(self):
        if not firebase_admin._apps:
            cred = credentials.Certificate('firebase_key.json')
            # print(f'cred: {cred}')
            firebase_admin.initialize_app(cred)

    def verify_firebase_token(self, id_token):
        try:                
            decoded_token = auth.verify_id_token(id_token)
            print(f"Token successfully decoded: {decoded_token}")
            uid = decoded_token['uid']            
            return uid
        
        except auth.InvalidIdTokenError as e:
            print(f"Invalid ID token error: {e}")
            return None
        
    # def create_user(self, email, password):
    #     try:
    #         user = auth.create_user(email=email, password=password)
    #         return user.uid
    #     except Exception as e:
    #         print(f"Error creating user: {e}")
    #         return None
    
    def get_user_by_uid(self, uid):
        try:
            user_record = auth.get_user(uid)
            return user_record
        except auth.UserNotFoundError:
            return None
        except Exception as e:
            print(f"Error retrieving user by UID: {e}")
            return None