from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample eBook data
ebooks = [
    {'id': 1, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year': 1925},
    {'id': 2, 'title': '1984', 'author': 'George Orwell', 'year': 1949},
    {'id': 3, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960},
    # Add more eBooks as needed
]

@app.route('/search', methods=['GET'])
def search_ebooks():
    search_query = request.args.get('search_query', '').lower()
    filtered_ebooks = [ebook for ebook in ebooks if search_query in ebook['title'].lower() or search_query in ebook['author'].lower()]
    return jsonify(filtered_ebooks)

@app.route('/ebook/<int:ebook_id>', methods=['GET'])
def get_ebook_details(ebook_id):
    ebook = next((ebook for ebook in ebooks if ebook['id'] == ebook_id), None)
    if ebook:
        return jsonify(ebook)
    return jsonify({'error': 'eBook not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)

import React, { useState, useEffect } from 'react';

const App = () => {
    const [searchQuery, setSearchQuery] = useState('');
    const [ebookList, setEbookList] = useState([]);
    const [ebookDetails, setEbookDetails] = useState(null);

    const handleSearch = async () => {
        const response = await fetch(`http://localhost:5000/search?search_query=${searchQuery}`);
        const data = await response.json();
        setEbookList(data);
    };

    const fetchEbookDetails = async (id) => {
        const response = await fetch(`http://localhost:5000/ebook/${id}`);
        const data = await response.json();
        setEbookDetails(data);
    };

    return (
        <div>
            <h1>eBook Library</h1>
            <input type='text' value={searchQuery} onChange={(e) => setSearchQuery(e.target.value)} />
            <button onClick={handleSearch}>Search</button>
            <ul>
                {ebookList.map(ebook => (
                    <li key={ebook.id} onClick={() => fetchEbookDetails(ebook.id)}>{ebook.title} by {ebook.author}</li>
                ))}
            </ul>
            {ebookDetails && <div><h2>{ebookDetails.title}</h2><p>Author: {ebookDetails.author}</p><p>Year: {ebookDetails.year}</p></div>}
        </div>
    );
};

export default App;
