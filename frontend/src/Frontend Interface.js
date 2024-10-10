from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({'message': 'Hello from the API!'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

import React, { useEffect, useState } from 'react';

const App = () => {
    const [data, setData] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            const response = await fetch('http://localhost:5000/api/data');
            const result = await response.json();
            setData(result.message);
        };
        fetchData();
    }, []);

    return (
        <div>
            <h1>Frontend Interface</h1>
            <p>{data ? data : 'Loading...'}</p>
        </div>
    );
};

export default App;

import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(<App />, document.getElementById('root'));