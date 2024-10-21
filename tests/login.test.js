const request = require('supertest');
const app = require('../server');
const User = require('../models/User');
const bcrypt = require('bcrypt');

beforeAll(async () => {
  await User.deleteMany();
  const hashedPassword = await bcrypt.hash('password123', 10);
  await User.create({ username: 'testuser', password: hashedPassword });
});

test('User can log in with valid credentials', async () => {
  const response = await request(app)
    .post('/login')
    .send({ username: 'testuser', password: 'password123' });
  expect(response.statusCode).toBe(200);
  expect(response.text).toBe('Login successful');
});

test('Invalid login attempts are handled gracefully', async () => {
  const response = await request(app)
    .post('/login')
    .send({ username: 'testuser', password: 'wrongpassword' });
  expect(response.statusCode).toBe(401);
  expect(response.text).toBe('Invalid credentials');
});