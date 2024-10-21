const db = require('../db');

exports.getSalesAndBillingData = async (startDate, endDate, carModel) => {
    const query = `SELECT * FROM sales WHERE date BETWEEN ? AND ? AND car_model = ?`;
    const results = await db.query(query, [startDate, endDate, carModel]);
    return results;
};
