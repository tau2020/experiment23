const express = require('express');
const bodyParser = require('body-parser');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');
const app = express();
const PORT = 3000;

app.use(bodyParser.json());

const users = {}; // In-memory user store
const SECRET_KEY = 'your_secret_key'; // Replace with your secret key

// User Registration
app.post('/register', async (req, res) => {
    const { username, password } = req.body;
    if (users[username]) {
        return res.status(400).json({ message: 'User already exists' });
    }
    const hashedPassword = await bcrypt.hash(password, 10);
    users[username] = { password: hashedPassword };
    res.status(201).json({ message: 'User registered successfully' });
});

// User Login
app.post('/login', async (req, res) => {
    const { username, password } = req.body;
    const user = users[username];
    if (!user || !(await bcrypt.compare(password, user.password))) {
        return res.status(401).json({ message: 'Invalid credentials' });
    }
    const authToken = jwt.sign({ username }, SECRET_KEY, { expiresIn: '1h' });
    res.json({ auth_token: authToken, user_info: { username } });
});

// Middleware to authenticate token
const authenticateToken = (req, res, next) => {
    const token = req.headers['authorization'] && req.headers['authorization'].split(' ')[1];
    if (!token) return res.sendStatus(401);
    jwt.verify(token, SECRET_KEY, (err, user) => {
        if (err) return res.sendStatus(403);
        req.user = user;
        next();
    });
};

// Example of a protected route
app.get('/protected', authenticateToken, (req, res) => {
    res.json({ message: 'This is a protected route', user: req.user });
});

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});