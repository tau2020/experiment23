from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///content.db'
db = SQLAlchemy(app)

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    content_type = db.Column(db.String(50), nullable=False)
    content_data = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {'id': self.id, 'user_id': self.user_id, 'content_type': self.content_type, 'content_data': self.content_data}

@app.route('/content', methods=['POST'])
def create_content():
    data = request.json
    new_content = Content(user_id=data['userId'], content_type=data['contentType'], content_data=data['contentData'])
    db.session.add(new_content)
    db.session.commit()
    return jsonify(new_content.to_dict()), 201

@app.route('/content', methods=['GET'])
def get_content():
    contents = Content.query.all()
    return jsonify([content.to_dict() for content in contents]), 200

@app.route('/content/<int:content_id>', methods=['GET'])
def get_content_detail(content_id):
    content = Content.query.get_or_404(content_id)
    return jsonify(content.to_dict()), 200

@app.route('/content/<int:content_id>', methods=['PUT'])
def update_content(content_id):
    data = request.json
    content = Content.query.get_or_404(content_id)
    content.content_data = data['contentData']
    db.session.commit()
    return jsonify(content.to_dict()), 200

@app.route('/content/<int:content_id>', methods=['DELETE'])
def delete_content(content_id):
    content = Content.query.get_or_404(content_id)
    db.session.delete(content)
    db.session.commit()
    return jsonify({'message': 'Content deleted'}), 204

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

import React, { useState, useEffect } from 'react';

const ContentManagement = () => {
    const [contentList, setContentList] = useState([]);
    const [contentDetail, setContentDetail] = useState(null);

    const fetchContent = async () => {
        const response = await fetch('/content');
        const data = await response.json();
        setContentList(data);
    };

    const fetchContentDetail = async (id) => {
        const response = await fetch(`/content/${id}`);
        const data = await response.json();
        setContentDetail(data);
    };

    useEffect(() => {
        fetchContent();
    }, []);

    return (
        <div>
            <h1>Content Management</h1>
            <ul>
                {contentList.map(content => (
                    <li key={content.id} onClick={() => fetchContentDetail(content.id)}>{content.content_data}</li>
                ))}
            </ul>
            {contentDetail && <div><h2>Content Detail</h2><p>{contentDetail.content_data}</p></div>}
        </div>
    );
};

export default ContentManagement;
