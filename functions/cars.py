from flask import jsonify
import psycopg2
from psycopg2 import extras
from sharedcode.db_connections import get_db_connection

def get_cars():
    connection = get_db_connection()

    cursor = connection.cursor(cursor_factory=extras.RealDictCursor)

    cursor.execute("SELECT * FROM cars")
    cars = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(cars)