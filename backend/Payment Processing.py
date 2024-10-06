const express = require('express');
const bodyParser = require('body-parser');
const { processPayment } = require('./paymentService');
const { authenticateUser } = require('./authService');
const { getUserProfile } = require('./userProfileService');

const app = express();
app.use(bodyParser.json());

app.post('/process-payment', async (req, res) => {
    const { paymentDetails, userId } = req.body;
    try {
        // Authenticate user
        const user = await authenticateUser(userId);
        if (!user) {
            return res.status(401).json({ message: 'User not authenticated' });
        }

        // Get user profile
        const userProfile = await getUserProfile(userId);
        if (!userProfile) {
            return res.status(404).json({ message: 'User profile not found' });
        }

        // Process payment
        const paymentConfirmation = await processPayment(paymentDetails, userProfile);
        return res.status(200).json({ paymentConfirmation });
    } catch (error) {
        return res.status(500).json({ message: 'Payment processing failed', error: error.message });
    }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Payment Processing service running on port ${PORT}`);
});

module.exports = app;