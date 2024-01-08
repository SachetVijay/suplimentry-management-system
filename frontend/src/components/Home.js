// src/components/Home.js
import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/Home.css';

const Home = () => {
  return (
    <div className="home-container">
      <h1>Welcome to Answer Sheet Manager</h1>
      <div className="buttons-container">
        <Link to="user/teacher/login" className="button">Login</Link>
        <Link to="user/teacher/signup" className="button">Signup</Link>
      </div>
    </div>
  );
}

export default Home;
