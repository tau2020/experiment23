from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# Simulated database of users
users = {1: 'user1@example.com', 2: 'user2@example.com'}

@app.route('/send_notification', methods=['POST'])
def send_notification():
    data = request.json
    user_id = data.get('user_id')
    notification_data = data.get('notification_data')

    if user_id not in users:
        return jsonify({'status': 'error', 'message': 'User not found'}), 404

    # Simulate sending notification (e.g., email, push notification)
    time.sleep(1)  # Simulate delay in sending notification

    return jsonify({'status': 'success', 'message': 'Notification sent'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)

// Frontend code (React.js)
import React, { useState } from 'react';

const NotificationSender = () => {
    const [userId, setUserId] = useState('');
    const [notificationData, setNotificationData] = useState('');
    const [status, setStatus] = useState('');

    const sendNotification = async () => {
        const response = await fetch('http://localhost:5000/send_notification', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ user_id: userId, notification_data: notificationData })
        });
        const result = await response.json();
        setStatus(result.message);
    };

    return (
        <div>
            <h1>Send Notification</h1>
            <input type='text' placeholder='User ID' value={userId} onChange={(e) => setUserId(e.target.value)} />
            <input type='text' placeholder='Notification Data' value={notificationData} onChange={(e) => setNotificationData(e.target.value)} />
            <button onClick={sendNotification}>Send</button>
            <p>{status}</p>
        </div>
    );
};

export default NotificationSender;