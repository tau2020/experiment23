from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# Simulated database interaction
class Database:
    def get_data(self):
        time.sleep(0.01)  # Simulate a delay
        return {'data': 'Hello, World!'}

db = Database()

@app.route('/api/data', methods=['GET'])
def get_data():
    start_time = time.time()
    data = db.get_data()
    processing_time = (time.time() - start_time) * 1000  # Convert to ms
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True, use_reloader=False)

import React, { useEffect, useState } from 'react';

const App = () => {
    const [data, setData] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            const response = await fetch('/api/data');
            const result = await response.json();
            setData(result.data);
        };
        fetchData();
    }, []);

    return <div>{data ? data : 'Loading...'}</div>;
};

export default App;
