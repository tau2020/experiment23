const express = require('express');
const { generateBill, downloadBill } = require('../controllers/billController');

const router = express.Router();

router.post('/', generateBill);
router.get('/:id/download', downloadBill);

module.exports = router;
