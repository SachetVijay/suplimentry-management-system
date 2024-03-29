// src/components/Card.js
import React from 'react';

const Card = ({ image, title, onClick, disabled = false, delete_=false}) => {
  return (
    <div className="card" onClick={onClick}>
      <img src={image} alt={title} className="card-image" />
      <div className="card-content">
        <h3>{title}</h3>
        {!disabled && !delete_ && <button>Open</button>}
        {!disabled && delete_ && <button className='delete-button'>Delete</button>}

      </div>
    </div>
  );
}

export default Card;
