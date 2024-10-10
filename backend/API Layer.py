from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/user', methods=['POST'])
def create_user():
    user_data = request.json
    # Here you would typically handle the user data, e.g., save to a database
    return jsonify({'message': 'User created successfully', 'data': user_data}), 201

@app.route('/api/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # Here you would typically retrieve user data from a database
    user_data = {'id': user_id, 'name': 'John Doe'}  # Example data
    return jsonify(user_data), 200

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000, threaded=True)