from flask import jsonify
import psycopg2
from psycopg2 import extras
from sharedcode.db_connections import get_db_connection
from sharedcode.query import car_by_id_query

def get_car(user_id):
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
    