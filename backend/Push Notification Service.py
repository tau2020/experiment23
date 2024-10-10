from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# Simulated database of user notifications
user_notifications = {}

@app.route('/send_notification', methods=['POST'])
def send_notification():
    data = request.json
    user_id = data.get('user_id')
    notification_data = data.get('notification_data')

    # Simulate sending notification (e.g., to a messaging service)
    time.sleep(0.5)  # Simulate delay

    # Store notification for the user
    if user_id not in user_notifications:
        user_notifications[user_id] = []
    user_notifications[user_id].append(notification_data)

    return jsonify({'notification_status': 'sent'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)

// Frontend Code (React.js)
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
        const data = await response.json();
        setStatus(data.notification_status);
    };

    return (
        <div>
            <h1>Send Notification</h1>
            <input type='text' placeholder='User ID' value={userId} onChange={(e) => setUserId(e.target.value)} />
            <input type='text' placeholder='Notification Data' value={notificationData} onChange={(e) => setNotificationData(e.target.value)} />
            <button onClick={sendNotification}>Send</button>
            <p>Status: {status}</p>
        </div>
    );
};

export default NotificationSender;