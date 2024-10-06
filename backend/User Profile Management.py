from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database for user profiles
user_profiles = {
    '1': {'name': 'John Doe', 'email': 'john@example.com'},
    '2': {'name': 'Jane Smith', 'email': 'jane@example.com'}
}

@app.route('/api/user/<user_id>', methods=['GET', 'PUT'])
def user_profile(user_id):
    if request.method == 'GET':
        profile = user_profiles.get(user_id)
        if profile:
            return jsonify(profile), 200
        return jsonify({'error': 'User not found'}), 404
    elif request.method == 'PUT':
        profile_data = request.json
        if user_id in user_profiles:
            user_profiles[user_id].update(profile_data)
            return jsonify(user_profiles[user_id]), 200
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)

import React, { useState, useEffect } from 'react';

const UserProfile = ({ userId }) => {
    const [profile, setProfile] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchProfile = async () => {
            try {
                const response = await fetch(`/api/user/${userId}`);
                if (!response.ok) throw new Error('User not found');
                const data = await response.json();
                setProfile(data);
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        };
        fetchProfile();
    }, [userId]);

    const handleUpdate = async (updatedData) => {
        try {
            const response = await fetch(`/api/user/${userId}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(updatedData),
            });
            if (!response.ok) throw new Error('Update failed');
            const data = await response.json();
            setProfile(data);
        } catch (err) {
            setError(err.message);
        }
    };

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error}</div>;

    return (
        <div>
            <h1>User Profile</h1>
            <p>Name: {profile.name}</p>
            <p>Email: {profile.email}</p>
            <button onClick={() => handleUpdate({ name: 'Updated Name' })}>Update Profile</button>
        </div>
    );
};

export default UserProfile;