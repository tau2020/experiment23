from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for demonstration
content_data = [
    {'id': 1, 'title': 'Flask Tutorial', 'tags': ['flask', 'python'], 'category': 'Programming'},
    {'id': 2, 'title': 'React Guide', 'tags': ['react', 'javascript'], 'category': 'Web Development'},
    {'id': 3, 'title': 'Machine Learning Basics', 'tags': ['ml', 'ai'], 'category': 'Data Science'},
    # Add more items as needed
]

@app.route('/search', methods=['GET'])
def search():
    search_query = request.args.get('searchQuery', '').lower()
    results = [item for item in content_data if 
               search_query in item['title'].lower() or 
               any(tag for tag in item['tags'] if search_query in tag.lower()) or 
               search_query in item['category'].lower()]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

// React Frontend
import React, { useState } from 'react';

const SearchComponent = () => {
    const [searchQuery, setSearchQuery] = useState('');
    const [searchResults, setSearchResults] = useState([]);

    const handleSearch = async () => {
        const response = await fetch(`http://localhost:5000/search?searchQuery=${searchQuery}`);
        const data = await response.json();
        setSearchResults(data);
    };

    return (
        <div>
            <input 
                type='text' 
                value={searchQuery} 
                onChange={(e) => setSearchQuery(e.target.value)} 
                placeholder='Search...'
            />
            <button onClick={handleSearch}>Search</button>
            <ul>
                {searchResults.map(result => (
                    <li key={result.id}>{result.title}</li>
                ))}
            </ul>
        </div>
    );
};

export default SearchComponent;

// In your main App component, import and use <SearchComponent />