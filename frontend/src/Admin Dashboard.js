from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock data for demonstration
admin_content_list = [
    {'id': 1, 'title': 'Post 1', 'content': 'Content of post 1'},
    {'id': 2, 'title': 'Post 2', 'content': 'Content of post 2'}
]

@app.route('/api/admin/content', methods=['GET'])
def get_admin_content():
    admin_auth_token = request.headers.get('Authorization')
    if admin_auth_token == 'Bearer valid_token':  # Simple auth check
        return jsonify(admin_content_list), 200
    return jsonify({'error': 'Unauthorized'}), 401

if __name__ == '__main__':
    app.run(debug=True, port=5000)

import React, { useEffect, useState } from 'react';

const AdminDashboard = () => {
    const [adminContent, setAdminContent] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchAdminContent = async () => {
            const response = await fetch('/api/admin/content', {
                method: 'GET',
                headers: {
                    'Authorization': 'Bearer valid_token'
                }
            });
            if (response.ok) {
                const data = await response.json();
                setAdminContent(data);
            }
            setLoading(false);
        };
        fetchAdminContent();
    }, []);

    if (loading) return <div>Loading...</div>;

    return (
        <div>
            <h1>Admin Dashboard</h1>
            <h2>Content List</h2>
            <ul>
                {adminContent.map(content => (
                    <li key={content.id}>{content.title}: {content.content}</li>
                ))}
            </ul>
        </div>
    );
};

export default AdminDashboard;

// In your main index.js file, you would render <AdminDashboard /> component.
