// src/components/TeacherAnswerSheet.js
import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import Card from './Card';
import axios from 'axios';



const TeacherAnswerSheet = () => {
  const [answersheet, setAnswersheet] = useState([])
  const [error, setError] = useState()

  const {subjectName, className}  = useParams();
  const fetch_class_data = async () => {
    try {
      const result = await axios.get(`http://127.0.0.1:5000/api/answersheet/${className}/${subjectName}`);
      setAnswersheet(result.data.answersheets.answersheets);
      
      // console.log(result.data);
    } catch (error) {
      setError(error.message);
    }
  };


  useEffect(() => {
    
    
    fetch_class_data();
    }, []);

    
    // const handleAdd = async(e) => {
    //   e.preventDefault();
    //   console.log('add clicked')
    // }

    const handleDelete = async(e, answerSheetName) => {
      try{
        e.preventDefault();
        const res = await axios.get(
          `http://127.0.0.1:5000/api/answersheet_delete/${className}/${subjectName}/${answerSheetName}`);
          setError(res.data)
        }catch(e){
          console.log(e);
          setError(e);
        }
        await fetch_class_data();
    };


    // const handleFileUpload = async (e) => {
    //   const file = e.target.files[0];
    //   const formData = new FormData();
    //   formData.append('file', file);
  
    //   try {
    //     const response = await axios.post('http://127.0.0.1:5000/api/upload', formData);
    //     console.log(response.data);
    //     // Now you can use the uploaded file information as needed
    //   } catch (error) {
    //     console.error('Error uploading file:', error);
    //   }
    // };

    const answerSheets = answersheet
  
  return (
    <div className="answer-sheet-container">
      <h1>{subjectName} Answer Sheets</h1>
      <div className="answer-sheets">
        {answerSheets.map((answerSheet) => (
          <Card
            key={answerSheet}
            title={answerSheet}
            onClick={(e)=>handleDelete(e, answerSheet)}
            delete_={true}
            />
        ))}
      </div>
      <Link to={`/add-answer-sheet/${className}/${subjectName}`} className="add-button">
        Add Answer Sheet
      </Link>
      {/* {error && <div style={{ color: 'red' }}>{error.message || 'An error occurred'}</div>} */}
    </div>
  );
}

export default TeacherAnswerSheet;
