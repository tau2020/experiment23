from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

MOVIE_API_URL = 'https://api.example.com/movies'  # Replace with actual movie database API URL

@app.route('/search', methods=['GET'])
def search_movies():
    query = request.args.get('query', '')
    filter_criteria = request.args.get('filter', '')
    response = requests.get(MOVIE_API_URL)
    movies = response.json()
    filtered_movies = [movie for movie in movies if query.lower() in movie['title'].lower()]
    if filter_criteria:
        filtered_movies = [movie for movie in filtered_movies if filter_criteria in movie['genre']]
    return jsonify(filtered_movies)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

import React, { useState, useEffect } from 'react';

const MovieSearch = () => {
    const [query, setQuery] = useState('');
    const [filter, setFilter] = useState('');
    const [movies, setMovies] = useState([]);

    const fetchMovies = async () => {
        const response = await fetch(`http://localhost:5000/search?query=${query}&filter=${filter}`);
        const data = await response.json();
        setMovies(data);
    };

    useEffect(() => {
        fetchMovies();
    }, [query, filter]);

    return (
        <div>
            <input type='text' placeholder='Search...' value={query} onChange={(e) => setQuery(e.target.value)} />
            <input type='text' placeholder='Filter by genre...' value={filter} onChange={(e) => setFilter(e.target.value)} />
            <ul>
                {movies.map(movie => <li key={movie.id}>{movie.title}</li>)}
            </ul>
        </div>
    );
};

export default MovieSearch;
