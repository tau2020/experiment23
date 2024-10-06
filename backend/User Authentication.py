const express = require('express');
const bodyParser = require('body-parser');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');
const mongoose = require('mongoose');

const app = express();
app.use(bodyParser.json());

const UserSchema = new mongoose.Schema({
  username: { type: String, required: true, unique: true },
  password: { type: String, required: true },
  email: { type: String, required: true, unique: true }
});

const User = mongoose.model('User', UserSchema);

const JWT_SECRET = 'your_jwt_secret';

app.post('/register', async (req, res) => {
  const { username, password, email } = req.body;
  const hashedPassword = await bcrypt.hash(password, 10);
  const user = new User({ username, password: hashedPassword, email });
  await user.save();
  res.status(201).json({ message: 'User registered successfully' });
});

app.post('/login', async (req, res) => {
  const { username, password } = req.body;
  const user = await User.findOne({ username });
  if (!user || !(await bcrypt.compare(password, user.password))) {
    return res.status(401).json({ message: 'Invalid credentials' });
  }
  const authToken = jwt.sign({ id: user._id }, JWT_SECRET, { expiresIn: '1h' });
  res.json({ authToken, userProfile: { username: user.username, email: user.email } });
});

app.get('/profile', async (req, res) => {
  const token = req.headers['authorization'];
  if (!token) return res.status(403).json({ message: 'No token provided' });
  jwt.verify(token, JWT_SECRET, async (err, decoded) => {
    if (err) return res.status(500).json({ message: 'Failed to authenticate token' });
    const user = await User.findById(decoded.id);
    res.json({ username: user.username, email: user.email });
  });
});

const PORT = process.env.PORT || 3000;
mongoose.connect('mongodb://localhost:27017/user_auth', { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => {
    app.listen(PORT, () => {
      console.log(`Server running on port ${PORT}`);
    });
  })
  .catch(err => console.error(err));