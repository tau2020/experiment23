from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

MOVIE_API_URL = 'https://api.example.com/movies'  # Replace with actual API URL

@app.route('/api/movies', methods=['GET'])
def get_movies():
    search_query = request.args.get('search', '')
    filter_option = request.args.get('filter', '')
    response = requests.get(MOVIE_API_URL, params={'search': search_query, 'filter': filter_option})
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True, port=5000)

// Frontend Code (React.js)
import React, { useState, useEffect } from 'react';

const MovieApp = () => {
    const [movies, setMovies] = useState([]);
    const [search, setSearch] = useState('');
    const [filter, setFilter] = useState('');

    const fetchMovies = async () => {
        const response = await fetch(`/api/movies?search=${search}&filter=${filter}`);
        const data = await response.json();
        setMovies(data);
    };

    useEffect(() => {
        fetchMovies();
    }, [search, filter]);

    return (
        <div>
            <h1>Movie Listings</h1>
            <input
                type='text'
                placeholder='Search Movies'
                value={search}
                onChange={(e) => setSearch(e.target.value)}
            />
            <select onChange={(e) => setFilter(e.target.value)}>
                <option value=''>All</option>
                <option value='action'>Action</option>
                <option value='comedy'>Comedy</option>
                <option value='drama'>Drama</option>
            </select>
            <ul>
                {movies.map(movie => (
                    <li key={movie.id}>{movie.title}</li>
                ))}
            </ul>
        </div>
    );
};

export default MovieApp;

// Main entry point (index.js)
import React from 'react';
import ReactDOM from 'react-dom';
import MovieApp from './MovieApp';

ReactDOM.render(<MovieApp />, document.getElementById('root'));