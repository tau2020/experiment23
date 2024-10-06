import React, { useState, useEffect } from 'react';
import axios from 'axios';

const UserInterface = () => {
  const [formData, setFormData] = useState({});
  const [displayData, setDisplayData] = useState(null);
  const [errorMessages, setErrorMessages] = useState('');

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('/api/user-actions', formData);
      setDisplayData(response.data);
      setErrorMessages('');
    } catch (error) {
      setErrorMessages('An error occurred. Please try again.');
    }
  };

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('/api/display-data');
        setDisplayData(response.data);
      } catch (error) {
        setErrorMessages('Failed to load data.');
      }
    };
    fetchData();
  }, []);

  return (
    <div>
      <h1>User Interface</h1>
      <form onSubmit={handleSubmit}>
        <input type='text' name='username' onChange={handleInputChange} placeholder='Username' required />
        <input type='password' name='password' onChange={handleInputChange} placeholder='Password' required />
        <button type='submit'>Submit</button>
      </form>
      {errorMessages && <p style={{ color: 'red' }}>{errorMessages}</p>}
      {displayData && <div>{JSON.stringify(displayData)}</div>}
    </div>
  );
};

export default UserInterface;