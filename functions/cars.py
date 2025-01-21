from flask import jsonify, request
import psycopg2
from psycopg2 import extras
from sharedcode.db_connections import get_db_connection
from sharedcode.query import cars_query
from sharedcode.firebase_auth import FirebaseAuthService

def get_cars():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"error": "Unauthorized"}), 401
    print(f'requestsss: {token}')
    firebase_auth_service = FirebaseAuthService()
    uid = firebase_auth_service.verify_firebase_token(token)
    if uid is None:
        return jsonify({"message": "Authentication failed"}), 401
    
    print(f'uid: {uid}') 
    
    connection = get_db_connection()

    cursor = connection.cursor(cursor_factory=extras.RealDictCursor)

    cursor.execute(cars_query)
    cars = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(cars)