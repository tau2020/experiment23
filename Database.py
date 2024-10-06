import sqlite3
import time
from flask import Flask, request, jsonify
from threading import Lock

app = Flask(__name__)

# Database connection setup
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
            result = cursor.fetchall()
            conn.commit()
        response_time = (time.time() - start_time) * 1000  # Convert to milliseconds
        return result, response_time

# API endpoint to handle data queries
@app.route('/query', methods=['POST'])
def query_data():
    data = request.json
    query = data.get('query')
    params = data.get('params', [])
    
    result, response_time = execute_query(query, params)
    
    if response_time > 100:
        return jsonify({'error': 'Response time exceeded 100ms'}), 500
    
    return jsonify({'result': result})

# API endpoint to handle data updates
@app.route('/update', methods=['POST'])
def update_data():
    data = request.json
    update_query = data.get('update_query')
    params = data.get('params', [])
    
    execute_query(update_query, params)
    
    return jsonify({'status': 'Update successful'})

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, threaded=True)