const request = require('supertest');
const app = require('../src/index');
const Bill = require('../src/models/Bill');

describe('Bill Controller', () => {
    afterEach(async () => {
        await Bill.deleteMany();
    });

    it('should generate a bill', async () => {
        const res = await request(app)
            .post('/api/bills')
            .send({ carId: '123', userId: '456', amount: 20000 });
        expect(res.statusCode).toEqual(201);
        expect(res.body).toHaveProperty('carId', '123');
    });
});
