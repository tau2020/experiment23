const paymentGateway = require('../utils/paymentGateway');

exports.processPayment = async (method, amount) => {
    if (method === 'credit_card') {
        return await paymentGateway.processCreditCardPayment(amount);
    } else if (method === 'paypal') {
        return await paymentGateway.processPayPalPayment(amount);
    } else {
        throw new Error('Unsupported payment method');
    }
};
