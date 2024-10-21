const express = require('express');
const Notification = require('../models/Notification');
const User = require('../models/User');

const router = express.Router();

router.post('/', async (req, res) => {
    const { userId, message, type } = req.body;
    const notification = new Notification({ userId, message, type });
    await notification.save();
    res.status(201).send(notification);
});

router.get('/:userId', async (req, res) => {
    const notifications = await Notification.find({ userId: req.params.userId });
    res.send(notifications);
});

router.patch('/opt-in/:userId', async (req, res) => {
    await User.updateOne({ _id: req.params.userId }, { notificationsEnabled: true });
    res.send({ message: 'Opted in for notifications' });
});

router.patch('/opt-out/:userId', async (req, res) => {
    await User.updateOne({ _id: req.params.userId }, { notificationsEnabled: false });
    res.send({ message: 'Opted out of notifications' });
});

module.exports = router;
