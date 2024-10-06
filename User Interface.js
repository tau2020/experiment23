import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './UserInterface.css'; // Assuming there's a CSS file for styling

const UserInterface = () => {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    // Fetch data from API on component mount
    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get('/api/data'); // Replace with actual API endpoint
                setData(response.data);
            } catch (err) {
                setError('Failed to fetch data');
            } finally {
                setLoading(false);
            }
        };

        fetchData();
    }, []);

    // Handle user interactions
    const handleUserAction = (action) => {
        // Process user action (e.g., button click)
        console.log(`User performed action: ${action}`);
        // Additional logic can be added here
    };

    // Render loading state, error state, or data
    if (loading) {
        return <div className="loading">Loading...</div>;
    }

    if (error) {
        return <div className="error">{error}</div>;
    }

    return (
        <div className="user-interface">
            <h1>User Interface</h1>
            <div className="data-container">
                {data && data.map((item) => (
                    <div key={item.id} className="data-item">
                        <h2>{item.title}</h2>
                        <p>{item.description}</p>
                        <button onClick={() => handleUserAction(item.id)}>Action</button>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default UserInterface;