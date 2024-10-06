const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

const app = express();
app.use(bodyParser.json());

// MongoDB schema for patient records
const patientSchema = new mongoose.Schema({
    patient_id: { type: String, required: true, unique: true },
    patient_data: { type: Object, required: true }
});

const Patient = mongoose.model('Patient', patientSchema);

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/patient_management', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Create or update patient record
app.post('/patients', async (req, res) => {
    const { patient_id, patient_data } = req.body;
    try {
        const patient = await Patient.findOneAndUpdate({ patient_id }, { patient_data }, { new: true, upsert: true });
        res.status(200).json(patient);
    } catch (error) {
        res.status(500).json({ error: 'Error saving patient record' });
    }
});

// Retrieve patient record
app.get('/patients/:patient_id', async (req, res) => {
    const { patient_id } = req.params;
    try {
        const patient = await Patient.findOne({ patient_id });
        if (!patient) {
            return res.status(404).json({ error: 'Patient not found' });
        }
        res.status(200).json(patient);
    } catch (error) {
        res.status(500).json({ error: 'Error retrieving patient record' });
    }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});