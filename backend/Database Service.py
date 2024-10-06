from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///images.db'
db = SQLAlchemy(app)

class ImageMetadata(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    upload_date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return { 'id': self.id, 'url': self.url, 'upload_date': self.upload_date.isoformat(), 'user_id': self.user_id }

@app.route('/upload', methods=['POST'])
def upload_image():
    data = request.json
    new_image = ImageMetadata(url=data['url'], upload_date=data['upload_date'], user_id=data['user_id'])
    db.session.add(new_image)
    db.session.commit()
    return jsonify(new_image.to_dict()), 201

@app.route('/images', methods=['GET'])
def get_images():
    images = ImageMetadata.query.all()
    return jsonify([image.to_dict() for image in images]), 200

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

import React, { useState, useEffect } from 'react';

const App = () => {
    const [images, setImages] = useState([]);
    const [url, setUrl] = useState('');
    const [userId, setUserId] = useState('');

    const fetchImages = async () => {
        const response = await fetch('/images');
        const data = await response.json();
        setImages(data);
    };

    const uploadImage = async () => {
        const response = await fetch('/upload', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ url, upload_date: new Date(), user_id: userId })
        });
        if (response.ok) {
            fetchImages();
        }
    };

    useEffect(() => {
        fetchImages();
    }, []);

    return (
        <div>
            <h1>Image Metadata</h1>
            <input type='text' placeholder='Image URL' value={url} onChange={(e) => setUrl(e.target.value)} />
            <input type='text' placeholder='User ID' value={userId} onChange={(e) => setUserId(e.target.value)} />
            <button onClick={uploadImage}>Upload Image</button>
            <ul>
                {images.map(image => (
                    <li key={image.id}>{image.url} - {image.upload_date} - {image.user_id}</li>
                ))}
            </ul>
        </div>
    );
};

export default App;