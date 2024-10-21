const Bill = require('../models/Bill');
const pdf = require('html-pdf');

exports.generateBill = async (req, res) => {
    const { carId, userId, amount } = req.body;
    const bill = new Bill({ carId, userId, amount });
    await bill.save();
    res.status(201).json(bill);
};

exports.downloadBill = async (req, res) => {
    const bill = await Bill.findById(req.params.id);
    if (!bill) return res.status(404).send('Bill not found');

    const html = `<h1>Bill for Car Purchase</h1><p>Car ID: ${bill.carId}</p><p>User ID: ${bill.userId}</p><p>Amount: ${bill.amount}</p>`;
    pdf.create(html).toStream((err, stream) => {
        if (err) return res.status(500).send(err);
        res.setHeader('Content-Type', 'application/pdf');
        stream.pipe(res);
    });
};
