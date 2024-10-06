import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import './App.css';

const FrontendUserInterface = ({ userActions, searchResults }) => {
  const [displayedProperties, setDisplayedProperties] = useState([]);
  const [userFeedback, setUserFeedback] = useState('');

  useEffect(() => {
    if (searchResults && searchResults.length > 0) {
      setDisplayedProperties(searchResults);
    }
  }, [searchResults]);

  const handleUserAction = (action) => {
    switch (action.type) {
      case 'LIKE_PROPERTY':
        setUserFeedback('You liked a property!');
        break;
      case 'SAVE_PROPERTY':
        setUserFeedback('Property saved!');
        break;
      default:
        setUserFeedback('Action not recognized.');
    }
  };

  return (
    <div className="frontend-ui">
      <h1>Property Listings</h1>
      <div className="property-list">
        {displayedProperties.map((property) => (
          <div key={property.id} className="property-item">
            <h2>{property.title}</h2>
            <p>{property.description}</p>
            <button onClick={() => handleUserAction({ type: 'LIKE_PROPERTY' })}>Like</button>
            <button onClick={() => handleUserAction({ type: 'SAVE_PROPERTY' })}>Save</button>
          </div>
        ))}
      </div>
      {userFeedback && <div className="user-feedback">{userFeedback}</div>}
    </div>
  );
};

FrontendUserInterface.propTypes = {
  userActions: PropTypes.array.isRequired,
  searchResults: PropTypes.array.isRequired,
};

export default FrontendUserInterface;