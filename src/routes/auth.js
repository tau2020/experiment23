const express = require('express');
const AuthenticationService = require('../authenticationService');
const router = express.Router();
const authService = new AuthenticationService(process.env.JWT_SECRET, '1h');

router.post('/register', async (req, res) => {
  try {
    const user = await authService.register(req.body);
    res.status(201).json(user);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

router.post('/login', async (req, res) => {
  try {
    const { token } = await authService.login(req.body.username, req.body.password);
    res.json({ token });
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

module.exports = router;