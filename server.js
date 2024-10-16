const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const authMiddleware = require('./middleware/auth');
const errorHandler = require('./middleware/errorHandler');
const portfolioRoutes = require('./routes/portfolio');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(bodyParser.json());
app.use(authMiddleware);
app.use('/api/portfolio', portfolioRoutes);
app.use(errorHandler);

mongoose.connect(process.env.MONGODB_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => {
    app.listen(PORT, () => {
      console.log(`Server is running on port ${PORT}`);
    });
  })
  .catch(err => console.error(err));