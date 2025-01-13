from flask import jsonify
import psycopg2
from psycopg2 import extras
from sharedcode.db_connections import get_db_connection
from sharedcode.query import users_query

def get_users():
    connection = get_db_connection()

    cursor = connection.cursor(cursor_factory=extras.RealDictCursor)

    cursor.execute(users_query)
    users = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(users)