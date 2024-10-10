from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cms.db'
db = SQLAlchemy(app)

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)

@app.route('/content', methods=['POST'])
def create_content():
    data = request.json
    new_content = Content(title=data['title'], body=data['body'])
    db.session.add(new_content)
    db.session.commit()
    return jsonify({'message': 'Content created successfully!'}), 201

@app.route('/content/<int:id>', methods=['PUT'])
def update_content(id):
    data = request.json
    content = Content.query.get_or_404(id)
    content.title = data['title']
    content.body = data['body']
    db.session.commit()
    return jsonify({'message': 'Content updated successfully!'}), 200

@app.route('/content', methods=['GET'])
def get_content():
    contents = Content.query.all()
    return jsonify([{'id': c.id, 'title': c.title, 'body': c.body} for c in contents]), 200

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, threaded=True)

import React, { useState, useEffect } from 'react';

const App = () => {
    const [contents, setContents] = useState([]);
    const [title, setTitle] = useState('');
    const [body, setBody] = useState('');

    const fetchContents = async () => {
        const response = await fetch('/content');
        const data = await response.json();
        setContents(data);
    };

    const createContent = async () => {
        await fetch('/content', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title, body })
        });
        fetchContents();
    };

    useEffect(() => {
        fetchContents();
    }, []);

    return (
        <div>
            <h1>Content Management System</h1>
            <input value={title} onChange={(e) => setTitle(e.target.value)} placeholder='Title' />
            <textarea value={body} onChange={(e) => setBody(e.target.value)} placeholder='Body'></textarea>
            <button onClick={createContent}>Create Content</button>
            <ul>
                {contents.map(content => (
                    <li key={content.id}>{content.title}: {content.body}</li>
                ))}
            </ul>
        </div>
    );
};

export default App;