from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Mock data for eBooks
ebooks = {
    '1': 'This is the content of eBook 1.',
    '2': 'This is the content of eBook 2.'
}

@app.route('/api/ebook/<ebook_id>', methods=['GET'])
def get_ebook(ebook_id):
    content = ebooks.get(ebook_id, 'eBook not found.')
    return jsonify({'content': content})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

// Frontend Code (React.js)
import React, { useEffect, useState } from 'react';

const ReadingInterface = ({ ebookId, userPreferences }) => {
    const [content, setContent] = useState('');

    useEffect(() => {
        const fetchEbook = async () => {
            const response = await fetch(`http://localhost:5000/api/ebook/${ebookId}`);
            const data = await response.json();
            setContent(data.content);
        };
        fetchEbook();
    }, [ebookId]);

    return (
        <div>
            <div style={{ whiteSpace: 'pre-wrap', fontSize: userPreferences.fontSize }}>
                {content}
            </div>
            <div>
                <button onClick={() => console.log('Previous')}>Previous</button>
                <button onClick={() => console.log('Next')}>Next</button>
            </div>
        </div>
    );
};

export default ReadingInterface;