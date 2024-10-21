const processCreditCardPayment = async (amount) => {
    // Simulate credit card processing
    return `Credit card payment of $${amount} processed successfully.`;
};

const processPayPalPayment = async (amount) => {
    // Simulate PayPal processing
    return `PayPal payment of $${amount} processed successfully.`;
};

module.exports = { processCreditCardPayment, processPayPalPayment };