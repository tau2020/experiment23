from flask import Flask, request, send_file
from PIL import Image
import io
import os

app = Flask(__name__)

@app.route('/process-image', methods=['POST'])
def process_image():
    if 'file' not in request.files:
        return {'error': 'No file part'}, 400
    file = request.files['file']
    if file.filename == '':
        return {'error': 'No selected file'}, 400
    
    # Processing parameters (example: resize)
    width = int(request.form.get('width', 800))
    height = int(request.form.get('height', 600))
    
    # Open the image file
    img = Image.open(file)
    
    # Resize the image
    img = img.resize((width, height), Image.ANTIALIAS)
    
    # Save the processed image to a bytes buffer
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='JPEG')
    img_byte_arr.seek(0)
    
    return send_file(img_byte_arr, mimetype='image/jpeg', as_attachment=True, download_name='processed_image.jpg')

if __name__ == '__main__':
    app.run(debug=True, port=5000)

import React, { useState } from 'react';

const ImageUpload = () => {
    const [file, setFile] = useState(null);
    const [width, setWidth] = useState(800);
    const [height, setHeight] = useState(600);

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append('file', file);
        formData.append('width', width);
        formData.append('height', height);

        const response = await fetch('/process-image', {
            method: 'POST',
            body: formData,
        });
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'processed_image.jpg';
        document.body.appendChild(a);
        a.click();
        a.remove();
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type='file' onChange={handleFileChange} required />
            <input type='number' value={width} onChange={(e) => setWidth(e.target.value)} placeholder='Width' />
            <input type='number' value={height} onChange={(e) => setHeight(e.target.value)} placeholder='Height' />
            <button type='submit'>Upload and Process</button>
        </form>
    );
};

export default ImageUpload;
