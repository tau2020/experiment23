from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reviews.db'
db = SQLAlchemy(app)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.String(50), nullable=False)
    user_review = db.Column(db.String(500), nullable=False)
    user_rating = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {'id': self.id, 'movie_id': self.movie_id, 'user_review': self.user_review, 'user_rating': self.user_rating}

@app.route('/reviews', methods=['POST'])
def submit_review():
    data = request.json
    new_review = Review(movie_id=data['movie_id'], user_review=data['user_review'], user_rating=data['user_rating'])
    db.session.add(new_review)
    db.session.commit()
    return jsonify({'message': 'Review submitted successfully!'}), 201

@app.route('/reviews/<movie_id>', methods=['GET'])
def get_reviews(movie_id):
    reviews = Review.query.filter_by(movie_id=movie_id).all()
    return jsonify([review.to_dict() for review in reviews]), 200

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=5000)

import React, { useState, useEffect } from 'react';

const ReviewSystem = () => {
    const [movieId, setMovieId] = useState('');
    const [userReview, setUserReview] = useState('');
    const [userRating, setUserRating] = useState(1);
    const [reviews, setReviews] = useState([]);

    const submitReview = async () => {
        const response = await fetch('/reviews', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ movie_id: movieId, user_review: userReview, user_rating: userRating })
        });
        if (response.ok) {
            fetchReviews();
        }
    };

    const fetchReviews = async () => {
        const response = await fetch(`/reviews/${movieId}`);
        const data = await response.json();
        setReviews(data);
    };

    useEffect(() => {
        if (movieId) fetchReviews();
    }, [movieId]);

    return (
        <div>
            <h1>Review and Rating System</h1>
            <input type='text' placeholder='Movie ID' value={movieId} onChange={(e) => setMovieId(e.target.value)} />
            <textarea placeholder='Your Review' value={userReview} onChange={(e) => setUserReview(e.target.value)}></textarea>
            <input type='number' min='1' max='5' value={userRating} onChange={(e) => setUserRating(e.target.value)} />
            <button onClick={submitReview}>Submit Review</button>
            <h2>Reviews:</h2>
            <ul>{reviews.map(review => <li key={review.id}>{review.user_review} - Rating: {review.user_rating}</li>)}</ul>
        </div>
    );
};

export default ReviewSystem;