from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample car data
cars = {
    '1': {'name': 'Car A', 'image': 'url_to_image_A', 'specs': {'color': 'red', 'engine': 'V6', 'year': 2020}},
    '2': {'name': 'Car B', 'image': 'url_to_image_B', 'specs': {'color': 'blue', 'engine': 'V8', 'year': 2021}}
}

@app.route('/api/cars/<car_id>', methods=['GET'])
def get_car_details(car_id):
    car_detail = cars.get(car_id)
    if car_detail:
        return jsonify(car_detail), 200
    return jsonify({'error': 'Car not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)

import React, { useEffect, useState } from 'react';

const CarDetails = ({ carId }) => {
    const [carDetail, setCarDetail] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchCarDetails = async () => {
            const response = await fetch(`/api/cars/${carId}`);
            if (response.ok) {
                const data = await response.json();
                setCarDetail(data);
            }
            setLoading(false);
        };
        fetchCarDetails();
    }, [carId]);

    if (loading) return <div>Loading...</div>;
    if (!carDetail) return <div>Car not found</div>;

    return (
        <div>
            <h1>{carDetail.name}</h1>
            <img src={carDetail.image} alt={carDetail.name} />
            <h2>Specifications:</h2>
            <ul>
                <li>Color: {carDetail.specs.color}</li>
                <li>Engine: {carDetail.specs.engine}</li>
                <li>Year: {carDetail.specs.year}</li>
            </ul>
        </div>
    );
};

export default CarDetails;