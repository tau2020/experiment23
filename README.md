# User Registration

## Installation
1. Clone the repository.
2. Run `npm install` to install dependencies.
3. Create a `.env` file in the root directory and add your MongoDB URI:
   `MONGODB_URI=mongodb://<username>:<password>@localhost:27017/user-registration`

## Running the Application
1. Run `npm start` to start the server.
2. Use Postman or any API client to test the registration endpoint at `http://localhost:5000/register`.

## Running with Docker
1. Run `docker-compose up` to start the application and MongoDB.

## Testing
Run `npm test` to execute the tests.