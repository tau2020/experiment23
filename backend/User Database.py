from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    preferences = db.Column(db.JSON, nullable=True)

    def __repr__(self):
        return f'<User {self.username}>'

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(username=data['username'], email=data['email'], preferences=data.get('preferences'))
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created'}), 201

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'username': user.username, 'email': user.email, 'preferences': user.preferences} for user in users])

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=5000)

import React, { useState, useEffect } from 'react';

const App = () => {
    const [users, setUsers] = useState([]);
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [preferences, setPreferences] = useState({});

    const fetchUsers = async () => {
        const response = await fetch('/users');
        const data = await response.json();
        setUsers(data);
    };

    const createUser = async () => {
        await fetch('/users', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, email, preferences }),
        });
        fetchUsers();
    };

    useEffect(() => {
        fetchUsers();
    }, []);

    return (
        <div>
            <h1>User Database</h1>
            <input value={username} onChange={(e) => setUsername(e.target.value)} placeholder='Username' />
            <input value={email} onChange={(e) => setEmail(e.target.value)} placeholder='Email' />
            <button onClick={createUser}>Create User</button>
            <ul>
                {users.map(user => <li key={user.id}>{user.username} - {user.email}</li>)}
            </ul>
        </div>
    );
};

export default App;