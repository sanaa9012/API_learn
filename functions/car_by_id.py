from flask import jsonify, request
import psycopg2
from psycopg2 import extras
from sharedcode.db_connections import get_db_connection
from sharedcode.query import car_by_id_query
from sharedcode.firebase_auth import FirebaseAuthService

def get_car():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"error": "Unauthorized"}), 401
    print(f'requestsss: {token}')
    firebase_auth_service = FirebaseAuthService()
    uid = firebase_auth_service.verify_firebase_token(token)
    if uid is None:
        return jsonify({"message": "Authentication failed"}), 401
    
    print(f'uid: {uid}')    
    
    user_id = request.args.get('user_id')
    
    connection = get_db_connection()
    cursor = connection.cursor(cursor_factory=extras.RealDictCursor)
    
    cursor.execute(car_by_id_query, (user_id,))
    cars = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    if cars:
        return jsonify(cars), 200
    else:
        return jsonify({"error": "Car with this User not found"}), 404
    