from flask import Flask, jsonify
import psycopg2
from psycopg2 import extras  
import os
from flask import request 
from functions.add_car import add_car
from functions.users import get_users
from functions.create_user import create_user
from functions.cars import get_cars
from functions.sales_data import sales_data
from functions.user_by_id import get_user   
from functions.car_by_id import get_car

app = Flask(__name__)

#Set up your database connection
def get_db_connection():
    conn = psycopg2.connect(
        dbname  =os.getenv('DBNAME'),
        user    =os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        host    =os.getenv('HOST'),
        port    =os.getenv('PORT')
    )
    return conn

@app.route('/users', methods=['GET'])
def allusers_route():
    return get_users()

@app.route('/sales_data', methods=['GET'])
def sales_data_route():
    return sales_data()

@app.route('/cars', methods=['GET'])
def cars_route():
    return get_cars()

@app.route('/create_user', methods=['POST'])
def create_user_route():
    return create_user()

@app.route('/add_car', methods=['POST'])
def add_car_route():
    return add_car()

@app.route('/users/<id>', methods=['GET'])
def get_user_route():
    return get_user()
    
@app.route('/cars/<user_id>', methods=['GET'])
def get_car_route():
    return get_car()

if __name__ == '__main__':
    app.run(debug=True)
    