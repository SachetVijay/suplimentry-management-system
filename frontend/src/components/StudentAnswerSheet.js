// src/components/StudentAnswerSheet.js
import React from 'react';

const StudentAnswerSheet = ({ subjectName }) => {
  const answerSheets = [
    // Add sample answer sheets for demonstration
    { id: 1, name: 'Answer Sheet 1' },
    { id: 2, name: 'Answer Sheet 2' },
  ];

  return (
    <div className="answer-sheet-container">
      <h1>{subjectName} Answer Sheets</h1>
      <div className="answer-sheets">
        {answerSheets.map((answerSheet) => (
          <div key={answerSheet.id} className="answer-sheet-card">
            <span>{answerSheet.name}</span>
          </div>
        ))}
      </div>
    </div>
  );
}

export default StudentAnswerSheet;
