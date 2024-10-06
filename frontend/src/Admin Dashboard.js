from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for car listings
car_listings = []

@app.route('/admin/login', methods=['POST'])
def admin_login():
    admin_credentials = request.json
    # Here you would validate the admin credentials
    return jsonify({'message': 'Login successful'}), 200

@app.route('/admin/cars', methods=['GET', 'POST'])
def manage_cars():
    if request.method == 'POST':
        car_data = request.json
        car_listings.append(car_data)
        return jsonify({'message': 'Car added successfully', 'updatedCarList': car_listings}), 201
    return jsonify({'carList': car_listings}), 200

if __name__ == '__main__':
    app.run(debug=True)

// AdminDashboard.js
import React, { useState, useEffect } from 'react';

const AdminDashboard = () => {
    const [carData, setCarData] = useState({});
    const [carList, setCarList] = useState([]);
    const [feedback, setFeedback] = useState('');

    const handleLogin = async (credentials) => {
        const response = await fetch('/admin/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(credentials)
        });
        const data = await response.json();
        setFeedback(data.message);
    };

    const handleAddCar = async () => {
        const response = await fetch('/admin/cars', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(carData)
        });
        const data = await response.json();
        setFeedback(data.message);
        setCarList(data.updatedCarList);
    };

    useEffect(() => {
        const fetchCars = async () => {
            const response = await fetch('/admin/cars');
            const data = await response.json();
            setCarList(data.carList);
        };
        fetchCars();
    }, []);

    return (
        <div>
            <h1>Admin Dashboard</h1>
            <div>{feedback}</div>
            <input type='text' placeholder='Car Data' onChange={(e) => setCarData(e.target.value)} />
            <button onClick={handleAddCar}>Add Car</button>
            <ul>
                {carList.map((car, index) => <li key={index}>{JSON.stringify(car)}</li>)}
            </ul>
        </div>
    );
};

export default AdminDashboard;

// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import AdminDashboard from './AdminDashboard';

ReactDOM.render(<AdminDashboard />, document.getElementById('root'));