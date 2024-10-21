const { Parser } = require('json2csv');

exports.exportToCSV = (data) => {
    const json2csvParser = new Parser();
    return json2csvParser.parse(data);
};
