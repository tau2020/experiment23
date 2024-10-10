from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for user profiles
user_profiles = {}

@app.route('/api/user_profile/<user_id>', methods=['GET', 'POST'])
def manage_user_profile(user_id):
    if request.method == 'POST':
        profile_data = request.json
        user_profiles[user_id] = profile_data
        return jsonify({'updated_profile': user_profiles[user_id]}), 200
    elif request.method == 'GET':
        return jsonify({'profile_data': user_profiles.get(user_id, {})}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)

import React, { useState, useEffect } from 'react';

const UserProfile = ({ userId }) => {
    const [profileData, setProfileData] = useState({});

    useEffect(() => {
        fetch(`/api/user_profile/${userId}`)
            .then(response => response.json())
            .then(data => setProfileData(data.profile_data));
    }, [userId]);

    const updateProfile = (newData) => {
        fetch(`/api/user_profile/${userId}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(newData),
        })
            .then(response => response.json())
            .then(data => setProfileData(data.updated_profile));
    };

    return (
        <div>
            <h1>User Profile</h1>
            <pre>{JSON.stringify(profileData, null, 2)}</pre>
            <button onClick={() => updateProfile({ preferences: 'new preferences', readingHistory: [], bookmarks: [] })}>Update Profile</button>
        </div>
    );
};

export default UserProfile;