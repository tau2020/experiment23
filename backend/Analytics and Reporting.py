from flask import Flask, request, jsonify
import pandas as pd
import json

app = Flask(__name__)

# Sample user activity data
user_activity_data = []

@app.route('/analytics', methods=['POST'])
def analyze_data():
    global user_activity_data
    user_activity_data = request.json.get('user_activity_data', [])
    if not user_activity_data:
        return jsonify({'error': 'No data provided'}), 400
    
    # Convert to DataFrame for analysis
    df = pd.DataFrame(user_activity_data)
    report = generate_report(df)
    return jsonify(report)


def generate_report(df):
    # Example analysis: count of activities per user
    report = df.groupby('user_id').size().reset_index(name='activity_count')
    return report.to_dict(orient='records')

if __name__ == '__main__':
    app.run(debug=True, port=5000)


import React, { useState } from 'react';

const AnalyticsReport = () => {
    const [report, setReport] = useState([]);
    const [loading, setLoading] = useState(false);

    const fetchAnalytics = async (userActivityData) => {
        setLoading(true);
        const response = await fetch('http://localhost:5000/analytics', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_activity_data: userActivityData })
        });
        const data = await response.json();
        setReport(data);
        setLoading(false);
    };

    return (
        <div>
            <h1>Analytics Report</h1>
            <button onClick={() => fetchAnalytics([{ user_id: 'user1', activity: 'view' }, { user_id: 'user2', activity: 'download' }])}>Generate Report</button>
            {loading ? <p>Loading...</p> : <pre>{JSON.stringify(report, null, 2)}</pre>}
        </div>
    );
};

export default AnalyticsReport;
