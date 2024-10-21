const express = require('express');
const User = require('../models/User');
const router = express.Router();

router.put('/:id', async (req, res) => {
    try {
        const user = await User.findByIdAndUpdate(req.params.id, req.body, { new: true });
        if (!user) return res.status(404).send('User not found');
        res.status(200).send({ message: 'Profile updated successfully', user });
    } catch (error) {
        res.status(500).send('Server error');
    }
});

module.exports = router;
