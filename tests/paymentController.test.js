const request = require('supertest');
const app = require('../src/index');

describe('Payment Controller', () => {
    it('should process credit card payment', async () => {
        const response = await request(app)
            .post('/api/payments')
            .send({ method: 'credit_card', amount: 100 });
        expect(response.status).toBe(200);
        expect(response.body.confirmation).toContain('processed successfully');
    });

    it('should process PayPal payment', async () => {
        const response = await request(app)
            .post('/api/payments')
            .send({ method: 'paypal', amount: 50 });
        expect(response.status).toBe(200);
        expect(response.body.confirmation).toContain('processed successfully');
    });

    it('should return error for unsupported payment method', async () => {
        const response = await request(app)
            .post('/api/payments')
            .send({ method: 'bitcoin', amount: 100 });
        expect(response.status).toBe(500);
        expect(response.body.error).toBe('Unsupported payment method');
    });
});
