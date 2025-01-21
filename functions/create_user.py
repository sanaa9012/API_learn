from flask import jsonify, request
import psycopg2
from psycopg2 import extras
from sharedcode.db_connections import get_db_connection
from sharedcode.query import create_user_query
from sharedcode.firebase_auth import FirebaseAuthService

def create_user(request):
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"error": "Unauthorized"}), 401
    print(f'requestsss: {request.headers.get("Authorization")}')
    firebase_auth_service = FirebaseAuthService()
    uid = firebase_auth_service.verify_firebase_token(request.headers.get("Authorization"))
    if uid is None:
        return jsonify({"message": "Authentication failed"}), 401
        
    print(f'uid: {uid}')
    
    connection = get_db_connection()
    cursor = connection.cursor(cursor_factory=extras.RealDictCursor)
    
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    
    cursor.execute(create_user_query, (name, email))
    connection.commit()
    
    cursor.close()
    connection.close()
    
    return jsonify({"message": "User created successfully"}), 201
