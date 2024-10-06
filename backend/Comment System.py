from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comments.db'
db = SQLAlchemy(app)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content_id = db.Column(db.String(50), nullable=False)
    text = db.Column(db.String(500), nullable=False)
    approved = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {'id': self.id, 'content_id': self.content_id, 'text': self.text, 'approved': self.approved}

@app.route('/comments/<content_id>', methods=['GET', 'POST'])
def comments(content_id):
    if request.method == 'POST':
        data = request.json
        new_comment = Comment(content_id=content_id, text=data['text'], approved=False)
        db.session.add(new_comment)
        db.session.commit()
        return jsonify(new_comment.to_dict()), 201
    else:
        comments = Comment.query.filter_by(content_id=content_id, approved=True).all()
        return jsonify([comment.to_dict() for comment in comments])

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=5000)

import React, { useState, useEffect } from 'react';

const CommentSystem = ({ contentId }) => {
    const [comments, setComments] = useState([]);
    const [commentText, setCommentText] = useState('');

    useEffect(() => {
        fetch(`/comments/${contentId}`)
            .then(response => response.json())
            .then(data => setComments(data));
    }, [contentId]);

    const handleCommentSubmit = () => {
        fetch(`/comments/${contentId}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text: commentText })
        })
        .then(response => response.json())
        .then(newComment => {
            setComments([...comments, newComment]);
            setCommentText('');
        });
    };

    return (
        <div>
            <h3>Comments</h3>
            <div>
                {comments.map(comment => (
                    <div key={comment.id}>{comment.text}</div>
                ))}
            </div>
            <textarea value={commentText} onChange={(e) => setCommentText(e.target.value)} />
            <button onClick={handleCommentSubmit}>Submit</button>
        </div>
    );
};

export default CommentSystem;