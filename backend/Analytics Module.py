from flask import Flask, request, jsonify
import time
import threading

app = Flask(__name__)

# In-memory storage for user activity and performance metrics
user_activity = []
performance_metrics = []

# Function to process data and generate reports
def generate_report():
    time.sleep(5)  # Simulate report generation time
    return {
        'user_activity_count': len(user_activity),
        'performance_metrics_count': len(performance_metrics)
    }

@app.route('/track_activity', methods=['POST'])
def track_activity():
    data = request.json
    user_activity.append(data)
    return jsonify({'status': 'success'}), 200

@app.route('/track_performance', methods=['POST'])
def track_performance():
    data = request.json
    performance_metrics.append(data)
    return jsonify({'status': 'success'}), 200

@app.route('/generate_report', methods=['GET'])
def report():
    report_data = generate_report()
    return jsonify(report_data), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)

import React, { useState, useEffect } from 'react';

const App = () => {
    const [report, setReport] = useState(null);

    const trackActivity = async (activity) => {
        await fetch('/track_activity', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(activity)
        });
    };

    const trackPerformance = async (metric) => {
        await fetch('/track_performance', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(metric)
        });
    };

    const generateReport = async () => {
        const response = await fetch('/generate_report');
        const data = await response.json();
        setReport(data);
    };

    useEffect(() => {
        // Example tracking
        trackActivity({ action: 'page_view', timestamp: Date.now() });
        trackPerformance({ load_time: 200, timestamp: Date.now() });
    }, []);

    return (
        <div>
            <h1>Analytics Module</h1>
            <button onClick={generateReport}>Generate Report</button>
            {report && <pre>{JSON.stringify(report, null, 2)}</pre>}
        </div>
    );
};

export default App;