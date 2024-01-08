// src/components/TeacherDashboard.js
import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Card from './Card';
import axios from 'axios';

const TeacherDashboard = () => {
  const [class_, setClass_] = useState()
  const [error, setError] = useState()
  const history = useNavigate()

  // const navigateToAnswerSheet = (className, subjectName) => {
  //   // Use react-router-dom's useNavigate hook to navigate
  //   navigate(`/student-answer-sheet/${className}/${subjectName}`);
  // };
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
  // console.log(class_)
  // const subjects = class_
  

  return (
    <div className="teacher-dashboard-container">
      <h1>Teacher Dashboard</h1>
      <div className="dashboard-grid">
      {class_?.map((subject) => (
          <Card
            key={subject.class_name}
            image={subject.class_image}
            title={subject.class_name}
            onClick={() => history(`/teacher-subject/${subject.class_name}`)}
          />
        ))}
      </div>
      {error && <div style={{ color: 'red' }}>{error.message || 'An error occurred'}</div>}
    </div>
  );
}

export default TeacherDashboard;
