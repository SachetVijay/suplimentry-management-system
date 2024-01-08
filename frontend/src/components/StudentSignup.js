// src/components/Signup.js
import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import '../styles/AuthForms.css';
import axios from 'axios';

const StudentSignup = () => {
  const [user_name, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [class_, setClass_] = useState();
  const [class_name, setClass] = useState('')
  const [role, setRole] = useState('');
  const [error, setError] = useState('');
  const history = useNavigate();
  

  useEffect(() => {
    const fetch_class_data = async () => {
      try {
        const result = await axios.get('http://127.0.0.1:5000/api/class_data');
        setClass_(result.data);
        
        // console.log(result.data);
      } catch (error) {
        setError(error.message);
      }
    }
    fetch_class_data();
    }, []);


  const handleSignup = async(e) => {
    e.preventDefault();
    try{
      const config = {
        headers: {
          "Content-type": "application/json",
        }
      };
      const res = await axios.post(
        "http://127.0.0.1:5000/api/user/student/register",
        {user_name, password, class_name},
        config
        );
        history('/student-dashboard')
        setError(res.data)
      }catch(e){
        console.log(e);
        setError(e);
      }
  };

  return (
    <div className="signup-container">
      <h1>Signup</h1>
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
        
        <label htmlFor="class">Class:</label>
        <select id="class" value={class_name} onChange={(e) => setClass(e.target.value)}>
            {class_?.map((subject) => (
                <option value={subject.class_name} key={subject.class_name}>{subject.class_name}</option>
            ))}
          
        </select>

        <label htmlFor="role">Role:</label>
        <select id="role" value={role} onChange={(e) => setRole(e.target.value)}>
          {/* <option value="teacher">Teacher</option> */}
          <option value="student">Student</option>
            
        </select>

        <button type="button" onClick={handleSignup}>Signup</button>
      </form>
      {error && <div style={{ color: 'red' }}>{error.message || 'An error occurred'}</div>}
      <p>Already have an account? <Link to="/user/teacher/login">Login</Link></p>
    </div>
  );
}

export default StudentSignup;
