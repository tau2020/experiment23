const express = require('express');
const router = express.Router();
const Portfolio = require('../models/Portfolio');

router.get('/', async (req, res) => {
  try {
    const portfolios = await Portfolio.find();
    res.json(portfolios);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

router.post('/', async (req, res) => {
  const portfolio = new Portfolio(req.body);
  try {
    const savedPortfolio = await portfolio.save();
    res.status(201).json(savedPortfolio);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

module.exports = router;