from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for car listings
cars = [
    {'id': 1, 'make': 'Toyota', 'model': 'Camry', 'year': 2020},
    {'id': 2, 'make': 'Honda', 'model': 'Civic', 'year': 2019},
    {'id': 3, 'make': 'Ford', 'model': 'Mustang', 'year': 2021}
]

@app.route('/api/cars', methods=['GET'])
def get_cars():
    return jsonify(cars)

if __name__ == '__main__':
    app.run(debug=True)

import React, { useState, useEffect } from 'react';

const CarListing = () => {
    const [cars, setCars] = useState([]);
    const [userInput, setUserInput] = useState('');
    const [userFeedback, setUserFeedback] = useState('');

    useEffect(() => {
        fetch('/api/cars')
            .then(response => response.json())
            .then(data => setCars(data));
    }, []);

    const handleSearch = () => {
        const filteredCars = cars.filter(car =>
            car.make.toLowerCase().includes(userInput.toLowerCase()) ||
            car.model.toLowerCase().includes(userInput.toLowerCase())
        );
        setUserFeedback(`Found ${filteredCars.length} cars.`);
        setCars(filteredCars);
    };

    return (
        <div>
            <h1>Car Listings</h1>
            <input
                type='text'
                value={userInput}
                onChange={(e) => setUserInput(e.target.value)}
                placeholder='Search by make or model'
            />
            <button onClick={handleSearch}>Search</button>
            <p>{userFeedback}</p>
            <ul>
                {cars.map(car => (
                    <li key={car.id}>{car.year} {car.make} {car.model}</li>
                ))}
            </ul>
        </div>
    );
};

export default CarListing;

import ReactDOM from 'react-dom';
import CarListing from './CarListing';

ReactDOM.render(<CarListing />, document.getElementById('root'));