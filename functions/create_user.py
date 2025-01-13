from flask import jsonify, request
import psycopg2
from psycopg2 import extras
from sharedcode.db_connections import get_db_connection


def create_user():
    connection = get_db_connection()
    cursor = connection.cursor(cursor_factory=extras.RealDictCursor)
    
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    connection.commit()
    
    cursor.close()
    connection.close()
    
    return jsonify({"message": "User created successfully"}), 201
