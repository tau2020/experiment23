from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory storage for listings
listings = []

@app.route('/listings', methods=['POST'])
def create_listing():
    listing_data = request.json
    listings.append(listing_data)
    return jsonify(listing_data), 201

@app.route('/listings/<int:listing_id>', methods=['GET'])
def get_listing(listing_id):
    if 0 <= listing_id < len(listings):
        return jsonify(listings[listing_id])
    return jsonify({'error': 'Listing not found'}), 404

@app.route('/listings', methods=['GET'])
def get_all_listings():
    return jsonify(listings)

@app.route('/listings/<int:listing_id>', methods=['PUT'])
def update_listing(listing_id):
    if 0 <= listing_id < len(listings):
        listing_data = request.json
        listings[listing_id] = listing_data
        return jsonify(listing_data)
    return jsonify({'error': 'Listing not found'}), 404

@app.route('/listings/<int:listing_id>', methods=['DELETE'])
def delete_listing(listing_id):
    if 0 <= listing_id < len(listings):
        listings.pop(listing_id)
        return jsonify({'message': 'Listing deleted'}), 200
    return jsonify({'error': 'Listing not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)

import React, { useState, useEffect } from 'react';

const App = () => {
    const [listings, setListings] = useState([]);
    const [newListing, setNewListing] = useState({});

    const fetchListings = async () => {
        const response = await fetch('http://localhost:5000/listings');
        const data = await response.json();
        setListings(data);
    };

    const createListing = async () => {
        await fetch('http://localhost:5000/listings', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(newListing),
        });
        fetchListings();
    };

    useEffect(() => {
        fetchListings();
    }, []);

    return (
        <div>
            <h1>House Listings</h1>
            <input type='text' onChange={(e) => setNewListing({ ...newListing, name: e.target.value })} placeholder='Listing Name' />
            <button onClick={createListing}>Add Listing</button>
            <ul>
                {listings.map((listing, index) => (
                    <li key={index}>{listing.name}</li>
                ))}
            </ul>
        </div>
    );
};

export default App;
