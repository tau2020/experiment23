from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample image metadata
images = [
    {'id': 1, 'url': 'https://example.com/image1.jpg', 'title': 'Image 1'},
    {'id': 2, 'url': 'https://example.com/image2.jpg', 'title': 'Image 2'},
    {'id': 3, 'url': 'https://example.com/image3.jpg', 'title': 'Image 3'},
]

@app.route('/api/images', methods=['GET'])
def get_images():
    return jsonify(images)

if __name__ == '__main__':
    app.run(debug=True)

import React, { useEffect, useState } from 'react';

const Gallery = () => {
    const [images, setImages] = useState([]);
    const [filter, setFilter] = useState('');

    useEffect(() => {
        const fetchImages = async () => {
            const response = await fetch('/api/images');
            const data = await response.json();
            setImages(data);
        };
        fetchImages();
    }, []);

    const filteredImages = images.filter(image =>
        image.title.toLowerCase().includes(filter.toLowerCase())
    );

    return (
        <div>
            <input
                type='text'
                placeholder='Filter images'
                value={filter}
                onChange={(e) => setFilter(e.target.value)}
            />
            <div className='gallery'>
                {filteredImages.map(image => (
                    <div key={image.id} className='image-item'>
                        <img src={image.url} alt={image.title} />
                        <h3>{image.title}</h3>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Gallery;

import React from 'react';
import ReactDOM from 'react-dom';
import Gallery from './Gallery';

ReactDOM.render(<Gallery />, document.getElementById('root'));