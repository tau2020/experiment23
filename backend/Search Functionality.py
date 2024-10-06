const express = require('express');
const app = express();
const bodyParser = require('body-parser');

app.use(bodyParser.json());

let properties = []; // This would be your property data source

app.post('/search', (req, res) => {
    const searchCriteria = req.body;
    const results = properties.filter(property => {
        return Object.keys(searchCriteria).every(key => {
            return property[key] && property[key].toString().toLowerCase().includes(searchCriteria[key].toString().toLowerCase());
        });
    });
    res.json({ searchResults: results });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
