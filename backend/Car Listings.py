from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for car listings
car_list = [
    {'id': 1, 'make': 'Toyota', 'model': 'Camry', 'year': 2020, 'price': 24000},
    {'id': 2, 'make': 'Honda', 'model': 'Civic', 'year': 2019, 'price': 22000},
    {'id': 3, 'make': 'Ford', 'model': 'Mustang', 'year': 2021, 'price': 26000},
    # Add more sample cars as needed
]

@app.route('/api/cars', methods=['GET'])
def get_cars():
    search_criteria = request.args.get('search', '')
    filter_options = request.args.get('filter', '')
    filtered_cars = [car for car in car_list if search_criteria.lower() in car['make'].lower() or search_criteria.lower() in car['model'].lower()]
    # Implement filtering logic based on filter_options if needed
    return jsonify(filtered_cars)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

// Frontend code (React.js)
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
            <input type='text' placeholder='Search...' value={search} onChange={(e) => setSearch(e.target.value)} />
            <button onClick={fetchCars}>Search</button>
            <ul>
                {cars.map(car => (
                    <li key={car.id}>{car.year} {car.make} {car.model} - ${car.price}</li>
                ))}
            </ul>
        </div>
    );
};

export default CarListings;

// Main entry point (index.js)
import React from 'react';
import ReactDOM from 'react-dom';
import CarListings from './CarListings';

ReactDOM.render(<CarListings />, document.getElementById('root'));