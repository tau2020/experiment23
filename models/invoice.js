const mongoose = require('mongoose');

const invoiceSchema = new mongoose.Schema({
    userId: { type: String, required: true },
    amount: { type: Number, required: true },
    date: { type: Date, default: Date.now },
    status: { type: String, default: 'Paid' }
});

module.exports = mongoose.model('Invoice', invoiceSchema);