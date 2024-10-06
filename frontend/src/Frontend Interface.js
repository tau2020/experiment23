from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = []
cars = [{'id': 1, 'make': 'Toyota', 'model': 'Camry', 'year': 2020}, {'id': 2, 'make': 'Honda', 'model': 'Civic', 'year': 2019}]

@app.route('/register', methods=['POST'])
def register():
    user = request.json
    users.append(user)
    return jsonify({'message': 'User registered successfully!'}), 201

@app.route('/login', methods=['POST'])
def login():
    user = request.json
    if user in users:
        return jsonify({'message': 'Login successful!'}), 200
    return jsonify({'message': 'Invalid credentials!'}), 401

@app.route('/cars', methods=['GET'])
def get_cars():
    return jsonify(cars), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)

import React, { useState, useEffect } from 'react';

function App() {
    const [cars, setCars] = useState([]);
    const [userFeedback, setUserFeedback] = useState('');
    const [userInput, setUserInput] = useState({ username: '', password: '' });

    useEffect(() => {
        fetch('http://localhost:5000/cars')
            .then(response => response.json())
            .then(data => setCars(data));
    }, []);

    const handleRegister = () => {
        fetch('http://localhost:5000/register', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(userInput)
        })
        .then(response => response.json())
        .then(data => setUserFeedback(data.message));
    };

    const handleLogin = () => {
        fetch('http://localhost:5000/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(userInput)
        })
        .then(response => response.json())
        .then(data => setUserFeedback(data.message));
    };

    return (
        <div>
            <h1>Car Selling Website</h1>
            <input type='text' placeholder='Username' onChange={e => setUserInput({ ...userInput, username: e.target.value })} />
            <input type='password' placeholder='Password' onChange={e => setUserInput({ ...userInput, password: e.target.value })} />
            <button onClick={handleRegister}>Register</button>
            <button onClick={handleLogin}>Login</button>
            <p>{userFeedback}</p>
            <h2>Available Cars</h2>
            <ul>
                {cars.map(car => <li key={car.id}>{car.make} {car.model} ({car.year})</li>)}
            </ul>
        </div>
    );
}

export default App;