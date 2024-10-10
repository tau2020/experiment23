from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample eBook data
ebooks = [
    {'id': 1, 'title': 'Book One', 'author': 'Author A'},
    {'id': 2, 'title': 'Book Two', 'author': 'Author B'},
    {'id': 3, 'title': 'Book Three', 'author': 'Author C'}
]

@app.route('/api/ebooks', methods=['GET'])
def get_ebooks():
    user_id = request.args.get('user_id')
    # Here you would typically check user authentication and fetch user-specific eBooks
    return jsonify(ebooks)

if __name__ == '__main__':
    app.run(debug=True)

import React, { useEffect, useState } from 'react';

const App = () => {
    const [eBookList, setEBookList] = useState([]);

    useEffect(() => {
        const fetchEBooks = async () => {
            const response = await fetch('/api/ebooks?user_id=1');
            const data = await response.json();
            setEBookList(data);
        };
        fetchEBooks();
    }, []);

    return (
        <div>
            <h1>eBook Library</h1>
            <ul>
                {eBookList.map(ebook => (
                    <li key={ebook.id}>{ebook.title} by {ebook.author}</li>
                ))}
            </ul>
        </div>
    );
};

export default App;
