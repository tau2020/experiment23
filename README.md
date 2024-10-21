# Sales Reporting Feature

## Installation
1. Clone the repository.
2. Run `npm install` to install dependencies.
3. Set up the database using the provided `docker-compose.yml`.

## Running the Application
- To start the application, run `npm start`.
- To run tests, use `npm test`.

## API Endpoints
### Generate Report
- **POST** `/api/reports/generate`
- **Body:** `{ startDate: 'YYYY-MM-DD', endDate: 'YYYY-MM-DD', carModel: 'Model Name' }`
- **Response:** CSV file download.

## Docker
- To run the application with Docker, use `docker-compose up`.
