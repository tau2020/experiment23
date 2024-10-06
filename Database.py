import sqlite3
import time
from flask import Flask, request, jsonify
from threading import Lock

app = Flask(__name__)

# Database connection and initialization
DATABASE = 'user_data.db'
lock = Lock()

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                content TEXT
            )
        ''')
        conn.commit()

# Function to execute a query
def execute_query(query, params=()):
    with lock:
        start_time = time.time()
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            if query.strip().upper().startswith("SELECT"):
                results = cursor.fetchall()
                response_time = time.time() - start_time
                return results, response_time
            else:
                conn.commit()
                response_time = time.time() - start_time
                return cursor.rowcount, response_time

# API endpoint to handle data queries
@app.route('/query', methods=['POST'])
def query_data():
    data = request.json
    query = data.get('query')
    params = data.get('params', [])
    
    results, response_time = execute_query(query, params)
    
    if response_time > 0.1:
        return jsonify({'error': 'Response time exceeded 100ms'}), 500
    
    return jsonify({'results': results})

# API endpoint to handle data updates
@app.route('/update', methods=['POST'])
def update_data():
    data = request.json
    query = data.get('query')
    params = data.get('params', [])
    
    rowcount, response_time = execute_query(query, params)
    
    if response_time > 0.1:
        return jsonify({'error': 'Response time exceeded 100ms'}), 500
    
    return jsonify({'confirmation': f'{rowcount} rows updated'})

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)