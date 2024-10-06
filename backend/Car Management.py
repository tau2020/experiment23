from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

car_list = []

@app.route('/cars', methods=['GET', 'POST', 'PUT', 'DELETE'])
def manage_cars():
    if request.method == 'GET':
        return jsonify({'carList': car_list})
    elif request.method == 'POST':
        car_data = request.json
        car_list.append(car_data)
        return jsonify({'successMessage': 'Car added successfully', 'carList': car_list}), 201
    elif request.method == 'PUT':
        car_data = request.json
        for index, car in enumerate(car_list):
            if car['id'] == car_data['id']:
                car_list[index] = car_data
                return jsonify({'successMessage': 'Car updated successfully', 'carList': car_list})
        return jsonify({'successMessage': 'Car not found'}), 404
    elif request.method == 'DELETE':
        car_id = request.json['id']
        global car_list
        car_list = [car for car in car_list if car['id'] != car_id]
        return jsonify({'successMessage': 'Car deleted successfully', 'carList': car_list})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

import React, { useState, useEffect } from 'react';

const CarManagement = () => {
    const [carList, setCarList] = useState([]);
    const [carData, setCarData] = useState({ id: '', name: '', model: '' });

    const fetchCars = async () => {
        const response = await fetch('http://localhost:5000/cars');
        const data = await response.json();
        setCarList(data.carList);
    };

    useEffect(() => {
        fetchCars();
    }, []);

    const addCar = async () => {
        await fetch('http://localhost:5000/cars', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(carData),
        });
        fetchCars();
    };

    const editCar = async () => {
        await fetch('http://localhost:5000/cars', {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(carData),
        });
        fetchCars();
    };

    const deleteCar = async (id) => {
        await fetch('http://localhost:5000/cars', {
            method: 'DELETE',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ id }),
        });
        fetchCars();
    };

    return (
        <div>
            <h1>Car Management</h1>
            <input type='text' placeholder='Car ID' onChange={(e) => setCarData({ ...carData, id: e.target.value })} />
            <input type='text' placeholder='Car Name' onChange={(e) => setCarData({ ...carData, name: e.target.value })} />
            <input type='text' placeholder='Car Model' onChange={(e) => setCarData({ ...carData, model: e.target.value })} />
            <button onClick={addCar}>Add Car</button>
            <button onClick={editCar}>Edit Car</button>
            <h2>Car List</h2>
            <ul>
                {carList.map(car => (
                    <li key={car.id}>
                        {car.name} - {car.model} <button onClick={() => deleteCar(car.id)}>Delete</button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default CarManagement;
