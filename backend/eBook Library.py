from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample eBook data
ebooks = [
    {'id': 1, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'genre': 'Fiction'},
    {'id': 2, 'title': '1984', 'author': 'George Orwell', 'genre': 'Dystopian'},
    {'id': 3, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'genre': 'Fiction'},
    {'id': 4, 'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'genre': 'Fiction'},
    {'id': 5, 'title': 'Brave New World', 'author': 'Aldous Huxley', 'genre': 'Dystopian'}
]

@app.route('/api/ebooks', methods=['GET'])
def get_ebooks():
    search_query = request.args.get('search_query', '').lower()
    filter_options = request.args.getlist('filter_options')

    filtered_ebooks = [
        ebook for ebook in ebooks
        if (search_query in ebook['title'].lower() or search_query in ebook['author'].lower())
        and (not filter_options or ebook['genre'] in filter_options)
    ]

    return jsonify(filtered_ebooks)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

import React, { useState, useEffect } from 'react';

const EbookLibrary = () => {
    const [ebooks, setEbooks] = useState([]);
    const [searchQuery, setSearchQuery] = useState('');
    const [filterOptions, setFilterOptions] = useState([]);

    const fetchEbooks = async () => {
        const response = await fetch(`http://localhost:5000/api/ebooks?search_query=${searchQuery}&filter_options=${filterOptions.join(',')}`);
        const data = await response.json();
        setEbooks(data);
    };

    useEffect(() => {
        fetchEbooks();
    }, [searchQuery, filterOptions]);

    return (
        <div>
            <input
                type='text'
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                placeholder='Search eBooks...'
            />
            <div>
                <label>
                    <input type='checkbox' onChange={(e) => setFilterOptions(e.target.checked ? [...filterOptions, 'Fiction'] : filterOptions.filter(f => f !== 'Fiction'))} />
                    Fiction
                </label>
                <label>
                    <input type='checkbox' onChange={(e) => setFilterOptions(e.target.checked ? [...filterOptions, 'Dystopian'] : filterOptions.filter(f => f !== 'Dystopian'))} />
                    Dystopian
                </label>
            </div>
            <ul>
                {ebooks.map(ebook => (
                    <li key={ebook.id}>{ebook.title} by {ebook.author}</li>
                ))}
            </ul>
        </div>
    );
};

export default EbookLibrary;
