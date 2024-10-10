from flask import Flask, send_from_directory, request, jsonify
import os

app = Flask(__name__, static_folder='build')

@app.route('/<path:path>', methods=['GET'])
def serve_static(path):
    return send_from_directory(app.static_folder, path)

@app.route('/', methods=['GET'])
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)

// React Frontend Code
import React from 'react';
import ReactDOM from 'react-dom';

const App = () => {
    return (
        <div>
            <h1>Welcome to the Web Server</h1>
        </div>
    );
};

ReactDOM.render(<App />, document.getElementById('root'));