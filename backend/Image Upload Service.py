from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'status': 'fail', 'message': 'No file part'}), 400
    file = request.files['file']
    user_id = request.form.get('user_id')
    if file.filename == '':
        return jsonify({'status': 'fail', 'message': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        image_url = f'/uploads/{filename}'
        # Here you would typically save the image URL and user ID to the database
        return jsonify({'status': 'success', 'image_url': image_url}), 200
    return jsonify({'status': 'fail', 'message': 'File type not allowed'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)

// React Frontend
import React, { useState } from 'react';

const ImageUpload = () => {
    const [file, setFile] = useState(null);
    const [userId, setUserId] = useState('');
    const [uploadStatus, setUploadStatus] = useState('');

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleUserIdChange = (e) => {
        setUserId(e.target.value);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append('file', file);
        formData.append('user_id', userId);
        const response = await fetch('http://localhost:5000/upload', {
            method: 'POST',
            body: formData,
        });
        const data = await response.json();
        setUploadStatus(data);
    };

    return (
        <div>
            <h1>Image Upload</h1>
            <form onSubmit={handleSubmit}>
                <input type='file' onChange={handleFileChange} required />
                <input type='text' value={userId} onChange={handleUserIdChange} placeholder='User ID' required />
                <button type='submit'>Upload</button>
            </form>
            {uploadStatus && <div>{JSON.stringify(uploadStatus)}</div>}
        </div>
    );
};

export default ImageUpload;