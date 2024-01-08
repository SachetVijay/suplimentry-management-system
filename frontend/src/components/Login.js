// src/components/Login.js
import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import '../styles/AuthForms.css';

const Login = () => {
  const [user_name, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [role, setRole] = useState('teacher');
  const [error, setError] = useState('');
  const history = useNavigate();

  const handleLogin = async(e) => {
    e.preventDefault();
    // console.log(role)
    try{
      const config = {
        headers: {
          "Content-type": "application/json",
        }
      };
      
      if(role === 'teacher'){
        // console.log(role)
        await axios.post(
          "http://127.0.0.1:5000/api/user/teacher/login",
          {user_name, password},
          config
          );
          localStorage.setItem('user_name', user_name)
          // console.log(localStorage);
          history('/teacher-dashboard')
      } else if(role === 'student'){
        const resp = await axios.post(
          "http://127.0.0.1:5000/api/user/student/login",
          {user_name, password},
          config
          );
          localStorage.setItem('user_name', user_name)
          localStorage.setItem('class_name', resp.data.class_name)
          history('/student-dashboard')
      } else{
        console.log('error with role')
      }
      
      }catch(e){
        // console.log("errrrr");
        console.log(e);
        setError(e);
      }
  };
  

  return (
    <div className="login-container">
      <h1>Login</h1>
      <form>
        <label htmlFor="username">Username:</label>
        <input
          type="text"
          id="username"
          value={user_name}
          onChange={(e) => setUsername(e.target.value)}
        />

        <label htmlFor="password">Password:</label>
        <input
          type="password"
          id="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <label htmlFor="role">Role:</label>
        <select id="role" onChange={(e) => setRole(e.target.value)}>
          <option value="teacher">Teacher</option>
          <option value="student">Student</option>
        </select>

        <button type="button" onClick={handleLogin}>Login</button>
      
        {error && <div style={{ color: 'red' }}>{error.message || 'An error occurred'}</div>}

      </form>
      <p>Don't have an account? <Link to="/user/teacher/signup">Signup</Link></p>
    </div>
  );
}

export default Login;
