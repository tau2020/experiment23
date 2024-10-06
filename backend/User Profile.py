from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user profiles for demonstration purposes
user_profiles = {}  

@app.route('/update_profile', methods=['POST'])
def update_profile():
    data = request.json
    user_id = data.get('userId')
    profile_data = data.get('profileData')
    
    if user_id and profile_data:
        user_profiles[user_id] = profile_data
        return jsonify({'updatedProfile': user_profiles[user_id]}), 200
    return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)

import React, { useState } from 'react';

const UserProfile = () => {
    const [userId, setUserId] = useState('');
    const [profileData, setProfileData] = useState({});
    const [updatedProfile, setUpdatedProfile] = useState(null);

    const handleUpdate = async () => {
        const response = await fetch('http://localhost:5000/update_profile', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ userId, profileData }),
        });
        const data = await response.json();
        if (response.ok) {
            setUpdatedProfile(data.updatedProfile);
        } else {
            console.error(data.error);
        }
    };

    return (
        <div>
            <h1>User Profile</h1>
            <input type='text' placeholder='User ID' value={userId} onChange={(e) => setUserId(e.target.value)} />
            <input type='text' placeholder='Profile Data' value={JSON.stringify(profileData)} onChange={(e) => setProfileData(JSON.parse(e.target.value))} />
            <button onClick={handleUpdate}>Update Profile</button>
            {updatedProfile && <div>Updated Profile: {JSON.stringify(updatedProfile)}</div>}
        </div>
    );
};

export default UserProfile;
