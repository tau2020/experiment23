from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database for user profiles
user_profiles = {}  # userId: profileData

@app.route('/api/user/<userId>', methods=['GET', 'PUT'])
def user_profile(userId):
    if request.method == 'GET':
        profile = user_profiles.get(userId, None)
        if profile:
            return jsonify(profile), 200
        else:
            return jsonify({'error': 'User not found'}), 404
    elif request.method == 'PUT':
        profile_data = request.json
        user_profiles[userId] = profile_data
        return jsonify(profile_data), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)

// Frontend code (React.js)
import React, { useState, useEffect } from 'react';

const UserProfile = ({ userId }) => {
    const [profileData, setProfileData] = useState({});

    useEffect(() => {
        fetch(`/api/user/${userId}`)
            .then(response => response.json())
            .then(data => setProfileData(data));
    }, [userId]);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setProfileData({ ...profileData, [name]: value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        fetch(`/api/user/${userId}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(profileData),
        })
            .then(response => response.json())
            .then(data => setProfileData(data));
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type='text' name='name' value={profileData.name || ''} onChange={handleChange} placeholder='Name' />
            <input type='email' name='email' value={profileData.email || ''} onChange={handleChange} placeholder='Email' />
            <button type='submit'>Update Profile</button>
        </form>
    );
};

export default UserProfile;