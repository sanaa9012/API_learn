import psycopg2
from flask import jsonify
from psycopg2 import extras
from sharedcode.db_connections import get_db_connection

def sales_data():
    connection = get_db_connection()
    
    cursor = connection.cursor(cursor_factory=extras.RealDictCursor)
    
    cursor.execute("SELECT * FROM sales_data")
    sales_data = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    return jsonify(sales_data)