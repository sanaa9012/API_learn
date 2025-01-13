from flask import jsonify, request
import psycopg2
from psycopg2 import extras
from sharedcode.db_connections import get_db_connection
from sharedcode.query import create_user_query

def create_user():
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
