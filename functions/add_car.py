from flask import Flask, jsonify
import psycopg2
from psycopg2 import extras  
import os
from flask import request
from sharedcode.db_connections import get_db_connection 
from sharedcode.query import add_car_query

def add_car():
    connection = get_db_connection()
    cursor = connection.cursor(cursor_factory=extras.RealDictCursor)
    
    data = request.get_json()
    brand = data.get('brand')
    model = data.get('model')
    year = data.get('year')
    color = data.get('color')
    user_id = data.get('user_id')
    
    cursor.execute(add_car_query, (brand, model, year, color, user_id))
    connection.commit()
    
    cursor.close()
    connection.close()
    
    return jsonify({"message": "Car added successfully"}), 201