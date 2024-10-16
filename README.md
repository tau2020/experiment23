# Authentication Service

## Overview
This service manages user authentication and authorization for admin access using JWT and bcrypt.

## Installation
1. Clone the repository.
2. Run `npm install` to install dependencies.
3. Create a `.env` file with the following variables:
   - `JWT_SECRET`: Your secret key for JWT.
   - `MONGODB_URI`: Your MongoDB connection string.
   - `PORT`: (Optional) Port number to run the server.

## Usage
- To register a user, send a POST request to `/api/auth/register` with a JSON body containing `username` and `password`.
- To log in, send a POST request to `/api/auth/login` with a JSON body containing `username` and `password`. You will receive a JWT token in response.

## Deployment Commands
- To start the application, run `npm start`.