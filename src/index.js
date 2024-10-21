const express = require('express');
const mongoose = require('mongoose');
const notificationRoutes = require('./routes/notifications');

const app = express();
app.use(express.json());

mongoose.connect('mongodb://mongo:27017/notifications', { useNewUrlParser: true, useUnifiedTopology: true });

app.use('/api/notifications', notificationRoutes);

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
