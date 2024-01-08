// src/components/Card.js
import React from 'react';

const Card = ({ image, title, onClick }) => {
  return (
    <div className="card" onClick={onClick}>
      <img src={image} alt={title} className="card-image" />
      <div className="card-content">
        <h3>{title}</h3>
        <button>Open</button>
      </div>
    </div>
  );
}

export default Card;
