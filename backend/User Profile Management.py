from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for user profiles
user_profiles = {}

@app.route('/update_profile', methods=['POST'])
def update_profile():
    data = request.json
    user_id = data.get('user_id')
    profile_data = data.get('profile_data')

    if user_id is None or profile_data is None:
        return jsonify({'error': 'Invalid input'}), 400

    # Update the user profile
    user_profiles[user_id] = profile_data
    return jsonify({'updated_profile': user_profiles[user_id]}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)

import React, { useState } from 'react';

const UserProfile = () => {
    const [userId, setUserId] = useState('');
    const [profileData, setProfileData] = useState('');
    const [updatedProfile, setUpdatedProfile] = useState(null);

    const handleUpdateProfile = async () => {
        const response = await fetch('http://localhost:5000/update_profile', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ user_id: userId, profile_data: profileData })
        });
        const data = await response.json();
        setUpdatedProfile(data.updated_profile);
    };

    return (
        <div>
            <h1>User Profile Management</h1>
            <input type='text' placeholder='User ID' value={userId} onChange={(e) => setUserId(e.target.value)} />
            <input type='text' placeholder='Profile Data' value={profileData} onChange={(e) => setProfileData(e.target.value)} />
            <button onClick={handleUpdateProfile}>Update Profile</button>
            {updatedProfile && <div>Updated Profile: {JSON.stringify(updatedProfile)}</div>}
        </div>
    );
};

export default UserProfile;