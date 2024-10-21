const { getSalesAndBillingData } = require('../services/reportService');
const { exportToCSV } = require('../utils/csvExporter');

exports.generateReport = async (req, res) => {
    const { startDate, endDate, carModel } = req.body;
    try {
        const data = await getSalesAndBillingData(startDate, endDate, carModel);
        const csv = exportToCSV(data);
        res.header('Content-Type', 'text/csv');
        res.attachment('report.csv');
        res.send(csv);
    } catch (error) {
        res.status(500).send({ message: 'Error generating report', error });
    }
};
