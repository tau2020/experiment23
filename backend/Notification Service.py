import time
import json

class NotificationService:
    def __init__(self):
        self.notification_status = ""

    def send_notification(self, notification_data):
        start_time = time.time()
        # Simulate sending notification
        time.sleep(2)  # Simulate a delay in sending notification
        self.notification_status = "Notification sent successfully"
        end_time = time.time()
        if end_time - start_time > 5:
            self.notification_status = "Notification delivery failed: Timeout"
        return self.notification_status

if __name__ == '__main__':
    service = NotificationService()
    data = {'user_id': 1, 'message': 'Your appointment is scheduled for tomorrow at 10 AM.'}
    result = service.send_notification(data)
    print(json.dumps({'notification_status': result}))