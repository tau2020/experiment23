from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/user', methods=['POST'])
def create_user():
    user_data = request.json
    # Here you would typically process the user data and interact with the database
    # For demonstration, we will just return the received data
    return jsonify({'status': 'success', 'data': user_data}), 201

@app.route('/api/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # Here you would typically fetch the user data from the database
    # For demonstration, we will return a mock user
    mock_user = {'id': user_id, 'name': 'John Doe'}
    return jsonify({'status': 'success', 'data': mock_user}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000, threaded=True)