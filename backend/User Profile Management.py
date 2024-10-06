from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database for user profiles
user_profiles = {
    1: {'name': 'John Doe', 'email': 'john@example.com'},
    2: {'name': 'Jane Smith', 'email': 'jane@example.com'}
}

@app.route('/api/user/<int:userId>', methods=['GET', 'PUT'])
def manage_user_profile(userId):
    if request.method == 'GET':
        profile = user_profiles.get(userId)
        if profile:
            return jsonify(profile), 200
        else:
            return jsonify({'error': 'User not found'}), 404
    elif request.method == 'PUT':
        profile_data = request.json
        if userId in user_profiles:
            user_profiles[userId].update(profile_data)
            return jsonify(user_profiles[userId]), 200
        else:
            return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)

import React, { useState, useEffect } from 'react';

const UserProfile = ({ userId }) => {
    const [profile, setProfile] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetch(`/api/user/${userId}`)
            .then(response => response.json())
            .then(data => {
                setProfile(data);
                setLoading(false);
            })
            .catch(err => {
                setError(err);
                setLoading(false);
            });
    }, [userId]);

    const handleUpdate = () => {
        const updatedData = { name: 'Updated Name', email: 'updated@example.com' };
        fetch(`/api/user/${userId}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(updatedData)
        })
            .then(response => response.json())
            .then(data => setProfile(data))
            .catch(err => setError(err));
    };

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error.message}</div>;

    return (
        <div>
            <h1>User Profile</h1>
            <p>Name: {profile.name}</p>
            <p>Email: {profile.email}</p>
            <button onClick={handleUpdate}>Update Profile</button>
        </div>
    );
};

export default UserProfile;