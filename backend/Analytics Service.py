from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# In-memory storage for user interaction data
user_data = []

@app.route('/api/analytics', methods=['POST'])
def collect_data():
    data = request.json
    user_data.append(data)
    return jsonify({'message': 'Data collected successfully'}), 201

@app.route('/api/reports', methods=['GET'])
def generate_report():
    # Simulate report generation
    time.sleep(1)  # Simulating processing time
    report = {'total_interactions': len(user_data), 'data': user_data}
    return jsonify(report)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

// Frontend code (React.js)
import React, { useState, useEffect } from 'react';

const AnalyticsService = () => {
    const [data, setData] = useState([]);
    const [report, setReport] = useState(null);

    const collectData = async (interaction) => {
        const response = await fetch('/api/analytics', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(interaction)
        });
        return response.json();
    };

    const fetchReport = async () => {
        const response = await fetch('/api/reports');
        const reportData = await response.json();
        setReport(reportData);
    };

    useEffect(() => {
        // Simulate user interaction data collection
        const interaction = { userId: 1, action: 'click', timestamp: new Date() };
        collectData(interaction);
        fetchReport();
    }, []);

    return (
        <div>
            <h1>Analytics Service</h1>
            {report && <pre>{JSON.stringify(report, null, 2)}</pre>}
        </div>
    );
};

export default AnalyticsService;