from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample data for house listings
house_listings = [
    {'id': 1, 'location': 'New York', 'price': 500000, 'size': 1200},
    {'id': 2, 'location': 'Los Angeles', 'price': 700000, 'size': 1500},
    {'id': 3, 'location': 'Chicago', 'price': 300000, 'size': 900},
    # Add more sample listings as needed
]

@app.route('/search', methods=['POST'])
def search_houses():
    search_criteria = request.json
    results = []

    for house in house_listings:
        if (search_criteria.get('location') and search_criteria['location'].lower() not in house['location'].lower()):
            continue
        if (search_criteria.get('min_price') and house['price'] < search_criteria['min_price']):
            continue
        if (search_criteria.get('max_price') and house['price'] > search_criteria['max_price']):
            continue
        if (search_criteria.get('min_size') and house['size'] < search_criteria['min_size']):
            continue
        if (search_criteria.get('max_size') and house['size'] > search_criteria['max_size']):
            continue
        results.append(house)

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

// Frontend Code (React)
import React, { useState } from 'react';

const SearchComponent = () => {
    const [location, setLocation] = useState('');
    const [minPrice, setMinPrice] = useState('');
    const [maxPrice, setMaxPrice] = useState('');
    const [minSize, setMinSize] = useState('');
    const [maxSize, setMaxSize] = useState('');
    const [results, setResults] = useState([]);

    const handleSearch = async () => {
        const response = await fetch('http://localhost:5000/search', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                location,
                min_price: minPrice,
                max_price: maxPrice,
                min_size: minSize,
                max_size: maxSize
            })
        });
        const data = await response.json();
        setResults(data);
    };

    return (
        <div>
            <h1>Search Houses</h1>
            <input type='text' placeholder='Location' value={location} onChange={(e) => setLocation(e.target.value)} />
            <input type='number' placeholder='Min Price' value={minPrice} onChange={(e) => setMinPrice(e.target.value)} />
            <input type='number' placeholder='Max Price' value={maxPrice} onChange={(e) => setMaxPrice(e.target.value)} />
            <input type='number' placeholder='Min Size' value={minSize} onChange={(e) => setMinSize(e.target.value)} />
            <input type='number' placeholder='Max Size' value={maxSize} onChange={(e) => setMaxSize(e.target.value)} />
            <button onClick={handleSearch}>Search</button>
            <ul>
                {results.map(house => (
                    <li key={house.id}>{house.location} - ${house.price} - {house.size} sqft</li>
                ))}
            </ul>
        </div>
    );
};

export default SearchComponent;
