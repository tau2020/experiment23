from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, jwt_refresh_token_required

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], email=data['email'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity={'username': user.username})
        return jsonify({'authToken': access_token, 'userProfile': {'username': user.username, 'email': user.email}}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    current_user = get_jwt_identity()
    user = User.query.filter_by(username=current_user['username']).first()
    return jsonify({'username': user.username, 'email': user.email}), 200

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=5000)

import React, { useState } from 'react';
import axios from 'axios';

const AuthComponent = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');
    const [authToken, setAuthToken] = useState('');
    const [userProfile, setUserProfile] = useState({});

    const handleRegister = async () => {
        const response = await axios.post('/register', { username, password, email });
        console.log(response.data);
    };

    const handleLogin = async () => {
        const response = await axios.post('/login', { username, password });
        setAuthToken(response.data.authToken);
        setUserProfile(response.data.userProfile);
    };

    return (
        <div>
            <h2>User Authentication</h2>
            <input type='text' placeholder='Username' onChange={(e) => setUsername(e.target.value)} />
            <input type='password' placeholder='Password' onChange={(e) => setPassword(e.target.value)} />
            <input type='email' placeholder='Email' onChange={(e) => setEmail(e.target.value)} />
            <button onClick={handleRegister}>Register</button>
            <button onClick={handleLogin}>Login</button>
            {authToken && <div>Token: {authToken}</div>}
            {userProfile.username && <div>Welcome, {userProfile.username}</div>}
        </div>
    );
};

export default AuthComponent;
