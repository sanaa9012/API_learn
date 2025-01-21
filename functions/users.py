from flask import jsonify, request
import psycopg2
from psycopg2 import extras
from sharedcode.db_connections import get_db_connection
from sharedcode.query import users_query
from sharedcode.firebase_auth import FirebaseAuthService

def get_users():
    firebase_auth_service = FirebaseAuthService()
    token = request.headers.get("Authorization")
    
    uid = firebase_auth_service.verify_firebase_token(token)
    
    if uid == "Authentication failed":
        return jsonify({"message": "Authentication failed"}), 401    
    
    connection = get_db_connection()

    cursor = connection.cursor(cursor_factory=extras.RealDictCursor)

    cursor.execute(users_query)
    users = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(users)