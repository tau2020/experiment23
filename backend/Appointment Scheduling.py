const express = require('express');
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid');
const app = express();
app.use(bodyParser.json());

let appointments = {};

app.post('/appointments', (req, res) => {
    const { patient_id, appointment_data } = req.body;
    const appointment_id = uuidv4();
    appointments[appointment_id] = { patient_id, appointment_data, status: 'scheduled' };
    res.status(201).json({ appointment_confirmation: appointment_id, appointment_details: appointments[appointment_id] });
});

app.put('/appointments/:id', (req, res) => {
    const { id } = req.params;
    const { appointment_data } = req.body;
    if (appointments[id]) {
        appointments[id].appointment_data = appointment_data;
        res.json({ appointment_details: appointments[id] });
    } else {
        res.status(404).json({ error: 'Appointment not found' });
    }
});

app.delete('/appointments/:id', (req, res) => {
    const { id } = req.params;
    if (appointments[id]) {
        delete appointments[id];
        res.status(204).send();
    } else {
        res.status(404).json({ error: 'Appointment not found' });
    }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Appointment Scheduling service running on port ${PORT}`);
});