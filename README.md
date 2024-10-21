# Notification System

## Installation
1. Clone the repository.
2. Run `npm install` to install dependencies.

## Running the Application
1. Start the MongoDB service using Docker: `docker-compose up -d`
2. Start the application: `npm start`

## API Endpoints
- `POST /api/notifications`: Create a notification.
- `GET /api/notifications/:userId`: Get notifications for a user.
- `PATCH /api/notifications/opt-in/:userId`: Opt-in for notifications.
- `PATCH /api/notifications/opt-out/:userId`: Opt-out of notifications.

## Running Tests
Run `npm test` to execute the tests.
