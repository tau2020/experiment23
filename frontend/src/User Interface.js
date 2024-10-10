from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/data', methods=['GET'])
def get_data():
    # Simulate an API response
    return jsonify({'message': 'Hello, World!'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

import React, { useEffect, useState } from 'react';

const App = () => {
    const [data, setData] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            const response = await fetch('http://localhost:5000/api/data');
            const result = await response.json();
            setData(result);
        };
        fetchData();
    }, []);

    return (
        <div>
            <h1>User Interface</h1>
            {data ? <p>{data.message}</p> : <p>Loading...</p>}
        </div>
    );
};

export default App;