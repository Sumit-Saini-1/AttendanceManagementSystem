from flask import Flask, request, jsonify
import mysql.connector as sql
from flask_cors import CORS,cross_origin
from db import db
from user import User
from AttendanceManager import AttendanceManager

app = Flask(__name__)
CORS(app)


@app.route('/create', methods=['POST'])
@cross_origin(origins=[u"*"])
def create_entry():
    request_data = request.get_json()
    event = request_data['event']
    date = request_data['date']
    time = request_data['time']
    attendee = request_data['attendee']
    status = request_data['status']
    am = AttendanceManager()
    am.createEntry(event, date, time, attendee, status)
    return jsonify({'message': 'Entry created successfully'}), 200

@app.route('/show', methods=['GET'])
@cross_origin(origins=[u"*"])
def show_data():
    am = AttendanceManager()
    data = am.showData()
    return jsonify({'data': data}), 200


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Email and password are required!'}), 400

    user = User.get_user(email)
    if user and user['password'] == password:
        return jsonify({'message': 'Login successful!', 'user': user}), 200
    else:
        return jsonify({'message': 'Invalid email or password!'}), 401

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'message': 'All fields are required!'}), 400

    # Check if the user already exists
    if User.get_user(email):
        return jsonify({'message': 'User already exists!'}), 409

    # Create a new user
    User.create_user(username, email, password)
    return jsonify({'message': 'User created successfully!'}), 201



if __name__ == '__main__':
    app.run(debug=True)
