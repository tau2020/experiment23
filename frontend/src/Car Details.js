from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for car details
car_data = {
    '1': {'name': 'Toyota Camry', 'year': 2020, 'price': 24000, 'images': ['image1.jpg', 'image2.jpg'], 'seller': {'name': 'John Doe', 'contact': '123-456-7890'}},
    '2': {'name': 'Honda Accord', 'year': 2021, 'price': 26000, 'images': ['image3.jpg', 'image4.jpg'], 'seller': {'name': 'Jane Smith', 'contact': '987-654-3210'}}
}

@app.route('/api/car/<car_id>', methods=['GET'])
def get_car_details(car_id):
    car_detail = car_data.get(car_id)
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
            const response = await fetch(`/api/car/${carId}`);
            const data = await response.json();
            setCarDetail(data);
            setLoading(false);
        };
        fetchCarDetails();
    }, [carId]);

    if (loading) return <div>Loading...</div>;
    if (!carDetail) return <div>Car not found</div>;

    return (
        <div>
            <h1>{carDetail.name} ({carDetail.year})</h1>
            <p>Price: ${carDetail.price}</p>
            <div>
                {carDetail.images.map((image, index) => (
                    <img key={index} src={image} alt={carDetail.name} />
                ))}
            </div>
            <h2>Seller Information</h2>
            <p>Name: {carDetail.seller.name}</p>
            <p>Contact: {carDetail.seller.contact}</p>
        </div>
    );
};

export default CarDetails;