# User Profile Management

## Installation
1. Clone the repository.
2. Run `npm install` to install dependencies.

## Running the Application
1. Start the MongoDB service using Docker:
   ```bash
   docker-compose up -d
   ```
2. Start the application:
   ```bash
   npm start
   ```

## API Endpoints
- `PUT /api/users/:id` - Update user profile.

## Testing
Run tests using:
```bash
npm test
```