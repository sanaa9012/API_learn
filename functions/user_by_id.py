from flask import jsonify, request
import psycopg2
from psycopg2 import extras
from sharedcode.db_connections import get_db_connection
from sharedcode.query import user_by_id_query
from sharedcode.firebase_auth import FirebaseAuthService

def get_user(request):
    print(f"request: {request}")
    # return jsonify('success'), 200
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"error": "Unauthorized"}), 401
    
    firebase_auth_service = FirebaseAuthService()
    uid = firebase_auth_service.verify_firebase_token(token)
    print(f'uid from token: {uid}')
    
    if not uid or uid == None:
        return jsonify({"error": "Unauthorized"}), 401
    
    # return jsonify({"message": "User found"}), 200
        
    user_id = request.args.get('user_id')
    
    # connection = get_db_connection()
    # cursor = connection.cursor(cursor_factory=extras.RealDictCursor)
    
    # cursor.execute(user_by_id_query, (id,))
    # users = cursor.fetchone()
    
    # cursor.close()
    # connection.close()
    
    # if users:
    #     return jsonify(users), 200
    # else:
    #     return jsonify({"error": "User not found"}), 404