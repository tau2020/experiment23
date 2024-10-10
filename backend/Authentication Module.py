from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully!'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password, data['password']):
        session['user_id'] = user.id
        return jsonify({'message': 'Login successful!', 'user_id': user.id}), 200
    return jsonify({'message': 'Invalid credentials!'}), 401

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({'message': 'Logged out successfully!'}), 200

@app.route('/profile', methods=['GET'])
def profile():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        return jsonify({'username': user.username}), 200
    return jsonify({'message': 'User not logged in!'}), 401

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=5000)

import React, { useState } from 'react';
import axios from 'axios';

const App = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [message, setMessage] = useState('');

    const handleRegister = async () => {
        const response = await axios.post('/register', { username, password });
        setMessage(response.data.message);
    };

    const handleLogin = async () => {
        const response = await axios.post('/login', { username, password });
        setMessage(response.data.message);
    };

    return (
        <div>
            <h1>Authentication Module</h1>
            <input type='text' placeholder='Username' onChange={(e) => setUsername(e.target.value)} />
            <input type='password' placeholder='Password' onChange={(e) => setPassword(e.target.value)} />
            <button onClick={handleRegister}>Register</button>
            <button onClick={handleLogin}>Login</button>
            <p>{message}</p>
        </div>
    );
};

export default App;