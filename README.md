# Invoice Management System

## Installation
1. Clone the repository.
2. Run `npm install` to install dependencies.

## Running the Application
1. Start the MongoDB service using Docker: `docker-compose up -d`
2. Start the application: `npm start`
3. Access the API at `http://localhost:3000`

## API Endpoints
- `GET /invoices/:userId`: View invoices for a user.
- `POST /invoices`: Generate an invoice after payment.
- `POST /invoices/reprint/:invoiceId`: Request an invoice reprint.

## Running Tests
Run `npm test` to execute the tests.