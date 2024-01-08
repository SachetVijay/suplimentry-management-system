// src/components/StudentAnswerSheet.js
import React from 'react';
import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import Card from './Card';

const StudentAnswerSheet = () => {

  const [answersheet, setAnswersheet] = useState([])
  const [error, setError] = useState()
  const {subjectName, className}  = useParams();
  

  useEffect(() => {
    const fetch_class_data = async () => {
      try {
        // console.log('hi there')
        
        const result = await axios.get(`http://127.0.0.1:5000/api/answersheet/${className}/${subjectName}`);
        setAnswersheet(result.data.answersheets.answersheets);
        
        // console.log(result.data.answersheets.answersheets);
      } catch (error) {
        setError(error.message);
      }
    }
    fetch_class_data();
    }, []);

  // const answerSheets = answersheet.answersheets.answersheets
  // console.log(answersheet[0])
  const answerSheets = answersheet


  return (
    <div className="answer-sheet-container">
      <h1>{subjectName} Answer Sheets</h1>
      <div className="answer-sheets">
        {answerSheets.map((answerSheet) => (
          <Card
            key={answerSheet}
            title={answerSheet}
            onClick={console.log('Open Suplimentry')}
            disabled={true}
            />
          
        ))}
      </div>
      {error && <div style={{ color: 'red' }}>{error.message || 'An error occurred'}</div>}
    </div>
  );
}

export default StudentAnswerSheet;
