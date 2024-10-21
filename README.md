# Car Billing Application

## Installation
1. Clone the repository.
2. Run `npm install` to install dependencies.

## Running the Application
1. Start MongoDB using Docker: `docker-compose up -d`
2. Start the application: `npm start`

## API Endpoints
- `POST /api/bills`: Generate a bill for a car purchase.
- `GET /api/bills/:id/download`: Download the bill as a PDF.

## Testing
Run `npm test` to execute the tests.
