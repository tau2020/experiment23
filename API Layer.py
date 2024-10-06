import express from 'express';
import bodyParser from 'body-parser';
import { UserService } from './services/UserService'; // Assume UserService handles backend communication
import { Database } from './database/Database'; // Assume Database handles DB operations

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Middleware to handle CORS
app.use((req, res, next) => {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});

// Route to handle user registration
app.post('/api/register', async (req, res) => {
    const userData = req.body;
    try {
        const result = await UserService.registerUser(userData);
        res.status(201).json({ message: 'User registered successfully', data: result });
    } catch (error) {
        res.status(400).json({ message: 'Error registering user', error: error.message });
    }
});

// Route to handle user login
app.post('/api/login', async (req, res) => {
    const { username, password } = req.body;
    try {
        const token = await UserService.loginUser(username, password);
        res.status(200).json({ message: 'Login successful', token });
    } catch (error) {
        res.status(401).json({ message: 'Invalid credentials', error: error.message });
    }
});

// Route to fetch user data
app.get('/api/user/:id', async (req, res) => {
    const userId = req.params.id;
    try {
        const user = await UserService.getUserById(userId);
        res.status(200).json({ message: 'User data retrieved', data: user });
    } catch (error) {
        res.status(404).json({ message: 'User not found', error: error.message });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`API Layer running on port ${PORT}`);
});

// Performance monitoring middleware
app.use((req, res, next) => {
    const start = Date.now();
    res.on('finish', () => {
        const duration = Date.now() - start;
        if (duration > 200) {
            console.warn(`Request to ${req.path} took ${duration}ms`);
        }
    });
    next();
});

// Export the app for testing
export default app;