import axios from 'axios';

const APIClient = axios.create({
  baseURL: process.env.REACT_APP_API_URL,
  timeout: 10000,
});

APIClient.interceptors.request.use((config) => {
  // Add any custom headers or configurations here
  return config;
}, (error) => {
  return Promise.reject(error);
});

APIClient.interceptors.response.use((response) => {
  // Handle response data here
  return response.data;
}, (error) => {
  // Handle errors here
  return Promise.reject(error);
});

export default APIClient;