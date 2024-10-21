const paymentService = require('../services/paymentService');

exports.processPayment = async (req, res) => {
    try {
        const { method, amount } = req.body;
        const confirmation = await paymentService.processPayment(method, amount);
        res.status(200).json({ confirmation });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
};
