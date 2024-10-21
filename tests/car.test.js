const request = require('supertest');
const app = require('../server');
const mongoose = require('mongoose');

beforeAll(async () => {
  await mongoose.connect('mongodb://localhost:27017/carInventoryTest', { useNewUrlParser: true, useUnifiedTopology: true });
});

afterAll(async () => {
  await mongoose.connection.close();
});

describe('Car API', () => {
  it('should create a new car', async () => {
    const res = await request(app)
      .post('/cars')
      .send({ make: 'Toyota', model: 'Camry', year: 2020, price: 24000 });
    expect(res.statusCode).toEqual(201);
    expect(res.body).toHaveProperty('make', 'Toyota');
  });

  it('should fetch all cars', async () => {
    const res = await request(app).get('/cars');
    expect(res.statusCode).toEqual(200);
    expect(Array.isArray(res.body)).toBeTruthy();
  });
});