const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

const app = express();
app.use(bodyParser.json());

// MongoDB User Schema
const userSchema = new mongoose.Schema({
    user_id: { type: String, required: true, unique: true },
    user_data: { type: Object, required: true },
    role: { type: String, required: true },
    permissions: { type: [String], required: true }
});

const User = mongoose.model('User', userSchema);

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/user_management', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Endpoint to manage user profiles
app.post('/user', async (req, res) => {
    const { user_id, user_data } = req.body;
    try {
        const user = await User.findOneAndUpdate({ user_id }, { user_data }, { new: true, upsert: true });
        res.status(200).json({ user_profile: user });
    } catch (error) {
        res.status(500).json({ error: 'Error managing user profile' });
    }
});

// Endpoint to get role permissions
app.get('/user/:user_id/permissions', async (req, res) => {
    const { user_id } = req.params;
    try {
        const user = await User.findOne({ user_id });
        if (!user) return res.status(404).json({ error: 'User not found' });
        res.status(200).json({ role_permissions: user.permissions });
    } catch (error) {
        res.status(500).json({ error: 'Error fetching role permissions' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});