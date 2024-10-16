# API Client

## Overview
The API Client component facilitates communication between the frontend and backend using Axios for making REST API calls.

## Installation
To install the necessary dependencies, run:
```
npm install
```

## Usage
Import the APIClient in your components to make API calls:
```javascript
import APIClient from './apiClient';

APIClient.get('/endpoint')
  .then(data => console.log(data))
  .catch(error => console.error(error));
```

## Deployment Commands
To build the application for production, run:
```
npm run build
```

To start the application in development mode, run:
```
npm start
```

## Additional Information
Ensure that the environment variable `REACT_APP_API_URL` is set to your backend API URL.