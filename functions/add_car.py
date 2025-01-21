from flask import Flask, jsonify
import psycopg2
from psycopg2 import extras  
import os
from flask import request
from sharedcode.db_connections import get_db_connection 
from sharedcode.query import add_car_query
from sharedcode.firebase_auth import FirebaseAuthService

def add_car():
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
    
    data = request.get_json()
    brand = data.get('brand')
    model = data.get('model')
    year = data.get('year')
    color = data.get('color')
    user_id = data.get('user_id')
    
    if not all([brand, model, year, color, user_id]):
        return jsonify({"error": "Missing required fields"}), 400
    
    cursor.execute(add_car_query, (brand, model, year, color, user_id))
    connection.commit()
    
    cursor.close()
    connection.close()
    
    return jsonify({"message": "Car added successfully"}), 201