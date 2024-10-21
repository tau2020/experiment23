const request = require('supertest');
const app = require('../src/index');

describe('Notification API', () => {
    it('should create a notification', async () => {
        const res = await request(app)
            .post('/api/notifications')
            .send({ userId: '60d5ec49f1b2c8b1f8c8e1a1', message: 'Payment confirmed', type: 'payment' });
        expect(res.statusCode).toEqual(201);
    });

    it('should get notifications for a user', async () => {
        const res = await request(app)
            .get('/api/notifications/60d5ec49f1b2c8b1f8c8e1a1');
        expect(res.statusCode).toEqual(200);
    });
});
