from flask import Flask, request, jsonify
from time import sleep

app = Flask(__name__)

# Mock database
ebooks = {"1": {"title": "Sample eBook", "content": "This is a sample eBook content."}}
user_progress = {}
annotations = {}

@app.route('/read/<ebook_id>/<user_id>', methods=['GET'])
def read_ebook(ebook_id, user_id):
    sleep(2)  # Simulate loading time
    if ebook_id not in ebooks:
        return jsonify({'error': 'eBook not found'}), 404
    return jsonify({
        'title': ebooks[ebook_id]['title'],
        'content': ebooks[ebook_id]['content'],
        'reading_progress': user_progress.get(user_id, {}).get(ebook_id, 0),
        'annotations': annotations.get(user_id, {}).get(ebook_id, [])
    })

@app.route('/bookmark', methods=['POST'])
def bookmark():
    data = request.json
    user_id = data['user_id']
    ebook_id = data['ebook_id']
    progress = data['progress']
    if user_id not in user_progress:
        user_progress[user_id] = {}
    user_progress[user_id][ebook_id] = progress
    return jsonify({'message': 'Progress saved'}), 200

@app.route('/annotate', methods=['POST'])
def annotate():
    data = request.json
    user_id = data['user_id']
    ebook_id = data['ebook_id']
    note = data['note']
    if user_id not in annotations:
        annotations[user_id] = {}
    if ebook_id not in annotations[user_id]:
        annotations[user_id][ebook_id] = []
    annotations[user_id][ebook_id].append(note)
    return jsonify({'message': 'Annotation saved'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)

import React, { useState, useEffect } from 'react';

const eBookReader = ({ ebookId, userId }) => {
    const [ebook, setEbook] = useState(null);
    const [progress, setProgress] = useState(0);
    const [notes, setNotes] = useState([]);

    useEffect(() => {
        fetch(`http://localhost:5000/read/${ebookId}/${userId}`)
            .then(response => response.json())
            .then(data => {
                setEbook(data);
                setProgress(data.reading_progress);
                setNotes(data.annotations);
            });
    }, [ebookId, userId]);

    const saveBookmark = () => {
        fetch('http://localhost:5000/bookmark', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_id: userId, ebook_id: ebookId, progress })
        });
    };

    const addAnnotation = (note) => {
        fetch('http://localhost:5000/annotate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_id: userId, ebook_id: ebookId, note })
        });
        setNotes([...notes, note]);
    };

    return (
        <div>
            {ebook && <h1>{ebook.title}</h1>}
            {ebook && <p>{ebook.content}</p>}
            <button onClick={saveBookmark}>Bookmark Progress</button>
            <input type='text' placeholder='Add a note' onKeyDown={(e) => { if (e.key === 'Enter') addAnnotation(e.target.value); }} />
            <ul>{notes.map((note, index) => <li key={index}>{note}</li>)}</ul>
        </div>
    );
};

export default eBookReader;