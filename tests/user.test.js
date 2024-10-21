const request = require('supertest');
const app = require('../src/index');
const User = require('../src/models/User');

describe('User Profile Management', () => {
    it('should update user profile', async () => {
        const user = await User.create({ name: 'John Doe', email: 'john@example.com', password: 'password123' });
        const res = await request(app)
            .put(`/api/users/${user._id}`)
            .send({ name: 'Jane Doe' });
        expect(res.statusCode).toEqual(200);
        expect(res.body.message).toBe('Profile updated successfully');
        expect(res.body.user.name).toBe('Jane Doe');
    });
});
