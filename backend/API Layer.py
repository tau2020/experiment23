from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/user', methods=['POST'])
def handle_user_request():
    user_data = request.json
    # Process user data (e.g., save to database, authenticate, etc.)
    # For demonstration, we will just echo the data back
    if not user_data:
        return jsonify({'error': 'No user data provided'}), 400
    return jsonify({'message': 'User data processed', 'data': user_data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True, use_reloader=False)