from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample data for cars
cars = [
    {'id': 1, 'make': 'Toyota', 'model': 'Camry', 'year': 2020},
    {'id': 2, 'make': 'Honda', 'model': 'Civic', 'year': 2019},
    {'id': 3, 'make': 'Ford', 'model': 'Mustang', 'year': 2021},
    # Add more sample cars as needed
]

@app.route('/api/cars', methods=['GET'])
def get_cars():
    search_criteria = request.args.get('search', '').lower()
    filter_options = request.args.get('filter', '').lower()
    filtered_cars = [car for car in cars if 
                     (search_criteria in car['make'].lower() or 
                      search_criteria in car['model'].lower()) and 
                     (filter_options in car['year'] if filter_options else True)]
    return jsonify(filtered_cars)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

import React, { useState, useEffect } from 'react';

const CarListings = () => {
    const [cars, setCars] = useState([]);
    const [search, setSearch] = useState('');
    const [filter, setFilter] = useState('');

    const fetchCars = async () => {
        const response = await fetch(`http://localhost:5000/api/cars?search=${search}&filter=${filter}`);
        const data = await response.json();
        setCars(data);
    };

    useEffect(() => {
        fetchCars();
    }, [search, filter]);

    return (
        <div>
            <input 
                type='text' 
                placeholder='Search by make or model' 
                value={search} 
                onChange={(e) => setSearch(e.target.value)} 
            />
            <input 
                type='text' 
                placeholder='Filter by year' 
                value={filter} 
                onChange={(e) => setFilter(e.target.value)} 
            />
            <ul>
                {cars.map(car => (
                    <li key={car.id}>{car.year} {car.make} {car.model}</li>
                ))}
            </ul>
        </div>
    );
};

export default CarListings;

// In your main index.js file, import and render <CarListings /> component.