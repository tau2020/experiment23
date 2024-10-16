const request = require('supertest');
const app = require('../src/app');

describe('GET /api/example', () => {
  it('should respond with a 200 status and the expected data', async () => {
    const response = await request(app).get('/api/example');
    expect(response.status).toBe(200);
    expect(response.body).toEqual({ data: 'Expected Data' });
  });

  it('should respond with a 404 status for non-existing route', async () => {
    const response = await request(app).get('/api/non-existing');
    expect(response.status).toBe(404);
  });
});