const mongoose = require('mongoose');

const billSchema = new mongoose.Schema({
    carId: { type: String, required: true },
    userId: { type: String, required: true },
    amount: { type: Number, required: true },
}, { timestamps: true });

module.exports = mongoose.model('Bill', billSchema);
