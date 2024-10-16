require('dotenv').config();
const express = require('express');
const { connectDB } = require('./db');

const app = express();
app.use(express.json());

connectDB();

app.listen(process.env.PORT || 3000, () => {
  console.log('Server is running');
});