// src/components/StudentDashboard.js
import React, { useEffect, useState } from 'react';
import Card from './Card';
import axios from 'axios';

const StudentDashboard = () => {
  const [class_, setClass_] = useState()
  const [error, setError] = useState()
  useEffect(() => {
    const fetch_class_data = async () => {
      const config = {
        headers: {
          "Content-type": "application/json",
        }
      };
      try {
        const class_name = localStorage.getItem("class_name")
        const resp = await axios.post(
          "http://127.0.0.1:5000/api/student_class",
          {class_name},
          config
          );
        setClass_(resp.data)
      } catch (error) {
        setError(error.message);
      }
    }
    fetch_class_data();
    }, []);
  // const subjects = [
  //   { id: 1, image: 'math_image.jpg', title: 'Mathematics' },
  //   { id: 2, image: 'math_image.jpg', title: 'Mathematics' },
  //   { id: 3, image: 'math_image.jpg', title: 'Mathematics' },
  //   { id: 4, image: 'math_image.jpg', title: 'Mathematics' },
  //   { id: 5, image: 'math_image.jpg', title: 'Mathematics' },
  //   { id: 6, image: 'math_image.jpg', title: 'Mathematics' },
  //   { id: 7, image: 'math_image.jpg', title: 'Mathematics' },

  //   // Add more subjects as needed
  // ];

  return (
    <div className="student-dashboard-container">
      <h1>Student Dashboard</h1>
      <div className="dashboard-grid">
        {class_ && 
          <Card
            key={class_.class_name}
            image={class_.class_image}
            title={class_.class_name}
            onClick={() => console.log(`Open ${class_.title} dashboard`)}
          />
          }
      </div>
      {error && <div style={{ color: 'red' }}>{error.message || 'An error occurred'}</div>}
    </div>
  );
}

export default StudentDashboard;
