const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const Invoice = require('./models/invoice');

const app = express();
app.use(bodyParser.json());

mongoose.connect('mongodb://localhost/invoice_management', { useNewUrlParser: true, useUnifiedTopology: true });

app.get('/invoices/:userId', async (req, res) => {
    const invoices = await Invoice.find({ userId: req.params.userId });
    res.json(invoices);
});

app.post('/invoices', async (req, res) => {
    const invoice = new Invoice(req.body);
    await invoice.save();
    res.status(201).send(invoice);
});

app.post('/invoices/reprint/:invoiceId', async (req, res) => {
    const invoice = await Invoice.findById(req.params.invoiceId);
    // Logic to send invoice via email or download link
    res.send('Invoice reprint requested.');
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});