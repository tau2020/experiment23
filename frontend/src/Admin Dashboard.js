from flask import Flask, jsonify, request
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

# Mock data for demonstration
admin_data = {
    'car_listings': [],
    'user_accounts': [],
    'analytics': {}
}

@app.route('/admin/dashboard', methods=['POST'])
def admin_dashboard():
    start_time = time.time()
    admin_credentials = request.json.get('adminCredentials')
    # Here you would normally validate admin_credentials
    # Simulating data loading time
    time.sleep(0.1)  # Simulate loading time under 300ms
    response_time = time.time() - start_time
    if response_time < 0.3:
        return jsonify(admin_data), 200
    else:
        return jsonify({'error': 'Request timed out'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)

// Frontend Code (React.js)
import React, { useState, useEffect } from 'react';

const AdminDashboard = () => {
    const [adminData, setAdminData] = useState(null);
    const [loading, setLoading] = useState(true);

    const fetchAdminData = async () => {
        const response = await fetch('http://localhost:5000/admin/dashboard', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ adminCredentials: 'admin123' })
        });
        const data = await response.json();
        setAdminData(data);
        setLoading(false);
    };

    useEffect(() => {
        fetchAdminData();
    }, []);

    if (loading) return <div>Loading...</div>;

    return (
        <div>
            <h1>Admin Dashboard</h1>
            <h2>Car Listings</h2>
            <pre>{JSON.stringify(adminData.car_listings, null, 2)}</pre>
            <h2>User Accounts</h2>
            <pre>{JSON.stringify(adminData.user_accounts, null, 2)}</pre>
            <h2>Analytics</h2>
            <pre>{JSON.stringify(adminData.analytics, null, 2)}</pre>
        </div>
    );
};

export default AdminDashboard;
