const request = require('supertest');
const app = require('../server');
const Invoice = require('../models/invoice');

describe('Invoice API', () => {
    beforeAll(async () => {
        await Invoice.deleteMany();
    });

    it('should create an invoice', async () => {
        const res = await request(app)
            .post('/invoices')
            .send({ userId: '123', amount: 100 });
        expect(res.statusCode).toEqual(201);
        expect(res.body).toHaveProperty('userId', '123');
    });

    it('should fetch invoices for a user', async () => {
        await request(app)
            .post('/invoices')
            .send({ userId: '123', amount: 100 });
        const res = await request(app).get('/invoices/123');
        expect(res.statusCode).toEqual(200);
        expect(res.body.length).toBeGreaterThan(0);
    });
});