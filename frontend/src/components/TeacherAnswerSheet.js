// src/components/TeacherAnswerSheet.js
import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Card from './Card';
import axios from 'axios';


const TeacherAnswerSheet = ({ subjectName }) => {
  const [class_, setClass_] = useState()
  const [error, setError] = useState()
  const history = useNavigate()
  useEffect(() => {
    const fetch_class_data = async () => {
      try {
        const result = await axios.get('http://127.0.0.1:5000/api/answersheet/'+'class_name/'+'subject_name');
        setClass_(result.data);
        
        // console.log(result.data);
      } catch (error) {
        setError(error.message);
      }
    }
    fetch_class_data();
    }, []);
  
  return (
    <div className="answer-sheet-container">
      <h1>{subjectName} Answer Sheets</h1>
      <div className="answer-sheets">
        {answerSheets.map((answerSheet) => (
          <div key={answerSheet.id} className="answer-sheet-card">
            <span>{answerSheet.name}</span>
            <button className="delete-button">Delete</button>
          </div>
        ))}
      </div>
      <Link to="/add-answer-sheet" className="add-button">
        Add Answer Sheet
      </Link>
    </div>
  );
}

export default TeacherAnswerSheet;
