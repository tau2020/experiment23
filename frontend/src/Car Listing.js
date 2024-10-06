from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for car listings
car_list = [
    {'id': 1, 'make': 'Toyota', 'model': 'Camry', 'year': 2020, 'price': 24000},
    {'id': 2, 'make': 'Honda', 'model': 'Civic', 'year': 2019, 'price': 22000},
    {'id': 3, 'make': 'Ford', 'model': 'Mustang', 'year': 2021, 'price': 26000},
    # Add more car listings as needed
]

@app.route('/api/cars', methods=['GET'])
def get_cars():
    search_criteria = request.args.get('search', '')
    filter_options = request.args.get('filter', '')
    filtered_cars = [car for car in car_list if search_criteria.lower() in car['make'].lower() or search_criteria.lower() in car['model'].lower()]
    # Implement filtering logic based on filter_options if needed
    return jsonify(filtered_cars)

if __name__ == '__main__':
    app.run(debug=True)

import React, { useState, useEffect } from 'react';

const CarListing = () => {
    const [cars, setCars] = useState([]);
    const [search, setSearch] = useState('');

    const fetchCars = async () => {
        const response = await fetch(`/api/cars?search=${search}`);
        const data = await response.json();
        setCars(data);
    };

    useEffect(() => {
        fetchCars();
    }, [search]);

    return (
        <div>
            <input
                type='text'
                placeholder='Search cars...'
                value={search}
                onChange={(e) => setSearch(e.target.value)}
            />
            <ul>
                {cars.map(car => (
                    <li key={car.id}>{car.make} {car.model} ({car.year}) - ${car.price}</li>
                ))}
            </ul>
        </div>
    );
};

export default CarListing;
