from flask import jsonify
import psycopg2
from psycopg2 import extras
from sharedcode.db_connections import get_db_connection

def get_users():
    connection = get_db_connection()

    cursor = connection.cursor(cursor_factory=extras.RealDictCursor)

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(users)