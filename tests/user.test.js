const request = require('supertest');
const app = require('../server');

describe('User Registration', () => {
  it('should register a user with valid email and password', async () => {
    const response = await request(app)
      .post('/register')
      .send({ email: 'test@example.com', password: 'password123' });
    expect(response.statusCode).toBe(201);
    expect(response.body.message).toBe('User registered successfully!');
  });

  it('should return an error for duplicate email', async () => {
    await request(app)
      .post('/register')
      .send({ email: 'test@example.com', password: 'password123' });
    const response = await request(app)
      .post('/register')
      .send({ email: 'test@example.com', password: 'password123' });
    expect(response.statusCode).toBe(500);
    expect(response.body.message).toBe('Error registering user.');
  });
});