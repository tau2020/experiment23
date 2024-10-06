const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

const app = express();
app.use(bodyParser.json());

// MongoDB schema for clinical data
const clinicalDataSchema = new mongoose.Schema({
    patient_id: { type: String, required: true },
    clinical_data: { type: Object, required: true },
    created_at: { type: Date, default: Date.now }
});

const ClinicalData = mongoose.model('ClinicalData', clinicalDataSchema);

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/clinical_data', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Endpoint to store clinical data
app.post('/clinical-data', async (req, res) => {
    const { patient_id, clinical_data } = req.body;
    const newRecord = new ClinicalData({ patient_id, clinical_data });
    await newRecord.save();
    res.status(201).json({ message: 'Clinical data saved successfully' });
});

// Endpoint to retrieve clinical data
app.get('/clinical-data/:patient_id', async (req, res) => {
    const { patient_id } = req.params;
    const clinicalRecord = await ClinicalData.find({ patient_id });
    res.status(200).json(clinicalRecord);
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});