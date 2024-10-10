from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

@app.route('/users', methods=['GET', 'POST'])
def handle_users():
    if request.method == 'POST':
        data = request.json
        new_user = User(name=data['name'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created'}), 201
    else:
        users = User.query.all()
        return jsonify([{'id': user.id, 'name': user.name, 'email': user.email} for user in users])

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=5000)

import React, { useState, useEffect } from 'react';

const App = () => {
    const [users, setUsers] = useState([]);
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');

    useEffect(() => {
        fetch('/users')
            .then(response => response.json())
            .then(data => setUsers(data));
    }, []);

    const addUser = () => {
        fetch('/users', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, email })
        })
        .then(response => response.json())
        .then(() => {
            setUsers([...users, { name, email }]);
            setName('');
            setEmail('');
        });
    };

    return (
        <div>
            <h1>User List</h1>
            <ul>
                {users.map(user => <li key={user.id}>{user.name} - {user.email}</li>)}
            </ul>
            <input value={name} onChange={e => setName(e.target.value)} placeholder='Name' />
            <input value={email} onChange={e => setEmail(e.target.value)} placeholder='Email' />
            <button onClick={addUser}>Add User</button>
        </div>
    );
};

export default App;