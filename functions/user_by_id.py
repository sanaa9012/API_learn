from flask import jsonify
import psycopg2
from psycopg2 import extras
from sharedcode.db_connections import get_db_connection
from sharedcode.query import user_by_id_query

def get_user(id):
    connection = get_db_connection()
    cursor = connection.cursor(cursor_factory=extras.RealDictCursor)
    
    cursor.execute(user_by_id_query, (id,))
    users = cursor.fetchone()
    
    cursor.close()
    connection.close()
    
    if users:
        return jsonify(users), 200
    else:
        return jsonify({"error": "User not found"}), 404