from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

content_db = []

@app.route('/api/content', methods=['POST'])
def create_content():
    data = request.json
    content_db.append(data)
    return jsonify({'message': 'Content created', 'content': data}), 201

@app.route('/api/content/<int:content_id>', methods=['PUT'])
def update_content(content_id):
    data = request.json
    if content_id < len(content_db):
        content_db[content_id] = data
        return jsonify({'message': 'Content updated', 'content': data}), 200
    return jsonify({'message': 'Content not found'}), 404

@app.route('/api/content', methods=['GET'])
def get_content():
    return jsonify(content_db), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)