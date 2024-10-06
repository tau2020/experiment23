from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample car data
cars = [
    {'id': 1, 'make': 'Toyota', 'model': 'Camry', 'year': 2020},
    {'id': 2, 'make': 'Honda', 'model': 'Civic', 'year': 2019},
    {'id': 3, 'make': 'Ford', 'model': 'Mustang', 'year': 2021},
    {'id': 4, 'make': 'Chevrolet', 'model': 'Malibu', 'year': 2018},
    {'id': 5, 'make': 'Nissan', 'model': 'Altima', 'year': 2022}
]

@app.route('/api/cars', methods=['GET'])
def get_cars():
    search_criteria = request.args.get('search', '')
    filter_options = request.args.get('filter', '')
    filtered_cars = [car for car in cars if search_criteria.lower() in car['make'].lower() or search_criteria.lower() in car['model'].lower()]
    # Implement filtering logic based on filter_options if needed
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
            <input type='text' value={search} onChange={(e) => setSearch(e.target.value)} placeholder='Search cars...' />
            <button onClick={fetchCars}>Search</button>
            <ul>
                {cars.map(car => (
                    <li key={car.id}>{car.make} {car.model} ({car.year})</li>
                ))}
            </ul>
        </div>
    );
};

export default CarListings;

// In your main app file, import and use <CarListings /> component.