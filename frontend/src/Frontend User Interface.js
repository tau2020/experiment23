from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/content', methods=['GET'])
def get_content():
    # Simulate fetching content based on userId
    user_id = request.args.get('userId')
    content = {"message": "Welcome to the fan page!", "userId": user_id}
    return jsonify(content)

if __name__ == '__main__':
    app.run(debug=True)

import React, { useEffect, useState } from 'react';

const FanPage = ({ authToken, userId }) => {
    const [content, setContent] = useState(null);

    useEffect(() => {
        const fetchContent = async () => {
            const response = await fetch(`/api/content?userId=${userId}`, {
                headers: { 'Authorization': `Bearer ${authToken}` }
            });
            const data = await response.json();
            setContent(data);
        };
        fetchContent();
    }, [authToken, userId]);

    return (
        <div>
            <h1>Fan Page</h1>
            {content ? <p>{content.message}</p> : <p>Loading...</p>}
        </div>
    );
};

export default FanPage;