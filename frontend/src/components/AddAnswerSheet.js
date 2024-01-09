// src/components/AddAnswerSheet.js
import React, { useState } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

const AddAnswerSheet = () => {
  const [file, setFile] = useState(null);
  const {className, subjectName} = useParams();

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) {
      console.error('Please select a file.');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);


    try {
      const response = await axios.post(`http://127.0.0.1:5000/api/answersheet_add/${className}/${subjectName}`, 
      formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      console.log(response.data);
      // Handle the response as needed
    } catch (error) {
      console.error('Error uploading file:', error);
    }
  };

  return (
    <div className='add-sheet-container'>
      <h1>Add Answer Sheet</h1>
      <form>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
      </form>
    </div>
  );
};

export default AddAnswerSheet;
