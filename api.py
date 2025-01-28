from flask import Flask, jsonify, request
import psycopg2
from psycopg2 import extras  
import os
from flask import request 
from functions.add_car import add_car
from functions.users import get_users
from functions.cars import get_cars
from functions.sales_data import sales_data
from functions.user_by_id import get_user   
from functions.car_by_id import get_car
import firebase_admin
from firebase_admin import credentials, auth
from functions.create_user import create_user
from brevo.get_email import get_emails
from functions.get_similar import get_similar

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data['email']
    password = data['password']

    user = auth.create_user(email=email, password=password)
    return jsonify({"message": "User created", "uid": user.uid}), 201

@app.route('/send_welcome_emails', methods=['GET'])
def send_welcome_emails():
    result = get_emails()
    return jsonify(result)

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
    return create_user(request)

@app.route('/add_car', methods=['POST'])
def add_car_route():
    return add_car()

@app.route('/get_user', methods=['GET'])
def get_user_route():
    return get_user(request)
    
@app.route('/get_car', methods=['GET'])
def get_car_route():    
    return get_car()

@app.route('/get_similar', methods = ['GET'])
def get_similar_route():
    keyword = request.args.get('keyword')
    return get_similar(keyword)

if __name__ == '__main__':
    app.run(debug=True)