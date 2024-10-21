const mysql = require('mysql2/promise');

const pool = mysql.createPool({
    host: 'localhost',
    user: 'root',
    database: 'sales_db',
    password: 'password'
});

module.exports = pool;
