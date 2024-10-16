const mongoose = require('mongoose');
const Portfolio = require('../models/Portfolio');
const UserSubmission = require('../models/UserSubmission');
const Config = require('../models/Config');

const connectDB = async () => {
  try {
    await mongoose.connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true });
    console.log('MongoDB connected');
  } catch (error) {
    console.error('MongoDB connection error:', error);
    process.exit(1);
  }
};

const savePortfolio = async (portfolioData) => {
  const portfolio = new Portfolio(portfolioData);
  return await portfolio.save();
};

const saveUserSubmission = async (submissionData) => {
  const submission = new UserSubmission(submissionData);
  return await submission.save();
};

const getConfig = async (key) => {
  return await Config.findOne({ key });
};

module.exports = { connectDB, savePortfolio, saveUserSubmission, getConfig };