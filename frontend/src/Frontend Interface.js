import React, { useState, useEffect } from 'react';

const FrontendInterface = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://localhost:5000/api/data');
        if (!response.ok) throw new Error('Network response was not ok');
        const result = await response.json();
        setData(result);
      } catch (error) {
        setError(error);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, []);

  const handleUserInteraction = () => {
    // Handle user interaction logic here
    alert('User interaction handled!');
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <div>
      <h1>Frontend Interface</h1>
      <button onClick={handleUserInteraction}>Interact</button>
      <div>{JSON.stringify(data)}</div>
    </div>
  );
};

export default FrontendInterface;

// Flask Backend Code
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data')
def get_data():
    return jsonify({'message': 'Hello from the API!'})

if __name__ == '__main__':
    app.run(debug=True)