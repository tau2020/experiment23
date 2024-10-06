import React, { useState, useEffect } from 'react';
import axios from 'axios';

const PropertyListing = ({ propertyData, userId }) => {
  const [propertyList, setPropertyList] = useState([]);
  const [propertyDetails, setPropertyDetails] = useState(null);

  useEffect(() => {
    fetchProperties();
  }, []);

  const fetchProperties = async () => {
    try {
      const response = await axios.get(`/api/properties?userId=${userId}`);
      setPropertyList(response.data);
    } catch (error) {
      console.error('Error fetching properties:', error);
    }
  };

  const addProperty = async (newProperty) => {
    try {
      const response = await axios.post('/api/properties', newProperty);
      setPropertyList([...propertyList, response.data]);
    } catch (error) {
      console.error('Error adding property:', error);
    }
  };

  const editProperty = async (updatedProperty) => {
    try {
      const response = await axios.put(`/api/properties/${updatedProperty.id}`, updatedProperty);
      setPropertyList(propertyList.map(property => property.id === updatedProperty.id ? response.data : property));
    } catch (error) {
      console.error('Error editing property:', error);
    }
  };

  const deleteProperty = async (propertyId) => {
    try {
      await axios.delete(`/api/properties/${propertyId}`);
      setPropertyList(propertyList.filter(property => property.id !== propertyId));
    } catch (error) {
      console.error('Error deleting property:', error);
    }
  };

  return (
    <div>
      <h1>Property Listings</h1>
      <ul>
        {propertyList.map(property => (
          <li key={property.id} onClick={() => setPropertyDetails(property)}>
            {property.title}
          </li>
        ))}
      </ul>
      {/* Add/Edit/Delete functionality can be implemented here */}
    </div>
  );
};

export default PropertyListing;