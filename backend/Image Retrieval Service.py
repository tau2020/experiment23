from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///images.db'
db = SQLAlchemy(app)

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    url = db.Column(db.String(255), nullable=False)
    metadata = db.Column(db.JSON, nullable=False)

@app.route('/images', methods=['GET'])
def get_images():
    user_id = request.args.get('user_id')
    filter_params = request.args.to_dict(flat=False)
    images = Image.query.filter_by(user_id=user_id).all()
    result = [{'id': img.id, 'url': img.url, 'metadata': img.metadata} for img in images]
    return jsonify(result)

if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True, port=5000)

import React, { useEffect, useState } from 'react';

const ImageRetrieval = () => {
    const [images, setImages] = useState([]);
    const userId = 1; // Example user ID

    useEffect(() => {
        const fetchImages = async () => {
            const response = await fetch(`http://localhost:5000/images?user_id=${userId}`);
            const data = await response.json();
            setImages(data);
        };
        fetchImages();
    }, []);

    return (
        <div>
            <h1>Image Retrieval</h1>
            <ul>
                {images.map(image => (
                    <li key={image.id}>
                        <img src={image.url} alt={image.metadata.title} />
                        <p>{JSON.stringify(image.metadata)}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ImageRetrieval;
