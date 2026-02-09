// API Configuration
// Change these values to match your deployment environment

const API_CONFIG = {
  development: {
    baseURL: 'http://localhost:5000',
  },
  production: {
    baseURL: process.env.REACT_APP_API_URL || 'https://api.yourdomain.com',
  },
};

const environment = process.env.NODE_ENV || 'development';

export default API_CONFIG[environment];
