const request = require('supertest');
const app = require('../src/index');

describe('POST /api/reports/generate', () => {
    it('should generate a report', async () => {
        const response = await request(app)
            .post('/api/reports/generate')
            .send({ startDate: '2023-01-01', endDate: '2023-12-31', carModel: 'Model X' });
        expect(response.status).toBe(200);
        expect(response.header['content-type']).toBe('text/csv');
    });
});
