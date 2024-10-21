const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const billRoutes = require('./routes/billRoutes');

const app = express();
app.use(bodyParser.json());

mongoose.connect('mongodb://localhost:27017/car_billing', { useNewUrlParser: true, useUnifiedTopology: true });

app.use('/api/bills', billRoutes);

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
