from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    director = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {'id': self.id, 'title': self.title, 'director': self.director, 'year': self.year}

@app.route('/movies', methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    return jsonify([movie.to_dict() for movie in movies])

@app.route('/movies/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    return jsonify(movie.to_dict())

@app.route('/movies', methods=['POST'])
def add_movie():
    data = request.get_json()
    new_movie = Movie(title=data['title'], director=data['director'], year=data['year'])
    db.session.add(new_movie)
    db.session.commit()
    return jsonify(new_movie.to_dict()), 201

@app.route('/movies/<int:movie_id>', methods=['PUT'])
def update_movie(movie_id):
    data = request.get_json()
    movie = Movie.query.get_or_404(movie_id)
    movie.title = data['title']
    movie.director = data['director']
    movie.year = data['year']
    db.session.commit()
    return jsonify(movie.to_dict())

@app.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return jsonify({'message': 'Movie deleted successfully'}), 204

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=5000)

import React, { useEffect, useState } from 'react';

const MovieApp = () => {
    const [movies, setMovies] = useState([]);

    useEffect(() => {
        fetch('/movies')
            .then(response => response.json())
            .then(data => setMovies(data));
    }, []);

    const addMovie = (movie) => {
        fetch('/movies', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(movie)
        })
        .then(response => response.json())
        .then(newMovie => setMovies([...movies, newMovie]));
    };

    return (
        <div>
            <h1>Movie Database</h1>
            <ul>
                {movies.map(movie => (
                    <li key={movie.id}>{movie.title} by {movie.director} ({movie.year})</li>
                ))}
            </ul>
            {/* Add movie form and other functionalities can be added here */}
        </div>
    );
};

export default MovieApp;