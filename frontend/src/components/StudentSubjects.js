import React, { useEffect, useState } from 'react';
import Card from './Card';
import axios from 'axios';
import { useNavigate, useParams } from 'react-router-dom';

const StudentSubject = () => {
  const [subjects, setSubjects] = useState()
  const [error, setError] = useState()
  const history = useNavigate()
  const class_name = useParams();
//   console.log(class_name)
  
  useEffect(() => {
    const fetch_subjects_data = async () => {
      try {
        // const class_name = localStorage.getItem('class_name')
        const result = await axios.get(`http://127.0.0.1:5000/api/subject_data/${class_name.className}`);
        setSubjects(result.data);
        

        console.log(result);
      } catch (error) {
        setError(error.message);
      }
    }
    fetch_subjects_data();
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
      <h1>Subject Dashboard</h1>
      <div className="dashboard-grid">
        {subjects?.map((subject) => (
          <Card
            key={subject.subject_name}
            image={subject.subject_image}
            title={subject.subject_name}
            onClick={() => history(`/student-answer-sheet/${subject.class_name}/${subject.subject_name}`)}
          />
        ))}
      </div>
      {error && <div style={{ color: 'red' }}>{error.message || 'An error occurred'}</div>}
    </div>
  );
}

export default StudentSubject;
