const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

const app = express();
app.use(bodyParser.json());

// MongoDB User Schema
const userSchema = new mongoose.Schema({
  userId: { type: String, required: true, unique: true },
  name: String,
  email: String,
  phone: String
});

const User = mongoose.model('User', userSchema);

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/userProfileDB', { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('MongoDB connected'))
  .catch(err => console.error('MongoDB connection error:', err));

// View User Profile
app.get('/profile/:userId', async (req, res) => {
  const { userId } = req.params;
  try {
    const user = await User.findOne({ userId });
    if (!user) return res.status(404).json({ message: 'User not found' });
    res.json(user);
  } catch (error) {
    res.status(500).json({ message: 'Error retrieving user profile' });
  }
});

// Edit User Profile
app.put('/profile/:userId', async (req, res) => {
  const { userId } = req.params;
  const profileData = req.body;
  try {
    const updatedProfile = await User.findOneAndUpdate({ userId }, profileData, { new: true });
    if (!updatedProfile) return res.status(404).json({ message: 'User not found' });
    res.json(updatedProfile);
  } catch (error) {
    res.status(500).json({ message: 'Error updating user profile' });
  }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});