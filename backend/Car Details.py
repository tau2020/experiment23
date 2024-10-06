from flask import Flask, jsonify, request
import time

app = Flask(__name__)

# Mock data for car details
car_data = {
    '1': {'make': 'Toyota', 'model': 'Camry', 'year': 2020, 'color': 'Blue'},
    '2': {'make': 'Honda', 'model': 'Accord', 'year': 2021, 'color': 'Red'},
    '3': {'make': 'Ford', 'model': 'Mustang', 'year': 2019, 'color': 'Black'}
}

@app.route('/car/<carId>', methods=['GET'])
def get_car_details(carId):
    start_time = time.time()
    car_detail = car_data.get(carId)
    if car_detail:
        response = jsonify(car_detail)
    else:
        response = jsonify({'error': 'Car not found'}), 404
    elapsed_time = (time.time() - start_time) * 1000
    if elapsed_time > 200:
        print('Warning: Response time exceeded 200ms')
    return response

if __name__ == '__main__':
    app.run(debug=True, port=5000)

import React, { useEffect, useState } from 'react';

const CarDetails = ({ carId }) => {
    const [carDetail, setCarDetail] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchCarDetails = async () => {
            try {
                const response = await fetch(`http://localhost:5000/car/${carId}`);
                if (!response.ok) {
                    throw new Error('Car not found');
                }
                const data = await response.json();
                setCarDetail(data);
            } catch (err) {
                setError(err.message);
            }
        };
        fetchCarDetails();
    }, [carId]);

    if (error) {
        return <div>{error}</div>;
    }

    if (!carDetail) {
        return <div>Loading...</div>;
    }

    return (
        <div>
            <h1>Car Details</h1>
            <p>Make: {carDetail.make}</p>
            <p>Model: {carDetail.model}</p>
            <p>Year: {carDetail.year}</p>
            <p>Color: {carDetail.color}</p>
        </div>
    );
};

export default CarDetails;
