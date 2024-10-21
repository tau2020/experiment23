const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(bodyParser.json());

mongoose.connect('mongodb://mongo:27017/carInventory', { useNewUrlParser: true, useUnifiedTopology: true });

const carSchema = new mongoose.Schema({
  make: String,
  model: String,
  year: Number,
  price: Number
});

const Car = mongoose.model('Car', carSchema);

app.post('/cars', async (req, res) => {
  const car = new Car(req.body);
  await car.save();
  res.status(201).send(car);
});

app.put('/cars/:id', async (req, res) => {
  const car = await Car.findByIdAndUpdate(req.params.id, req.body, { new: true });
  res.send(car);
});

app.delete('/cars/:id', async (req, res) => {
  await Car.findByIdAndDelete(req.params.id);
  res.status(204).send();
});

app.get('/cars', async (req, res) => {
  const cars = await Car.find();
  res.send(cars);
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});