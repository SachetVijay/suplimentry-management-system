// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import Home from './components/Home';
import Login from './components/Login';
import Signup from './components/Signup';
import TeacherDashboard from './components/TeacherDashboard'; // Import TeacherDashboard
import StudentDashboard from './components/StudentDashboard'; // Import StudentDashboard
import TeacherAnswerSheet from './components/TeacherAnswerSheet'; // Import TeacherAnswerSheet
import StudentAnswerSheet from './components/StudentAnswerSheet'; // Import StudentAnswerSheet
import TeacherSubjects from './components/TeacherSubjects'
import './App.css'






function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="user/teacher/login" element={<Login />} />
          <Route path="user/teacher/signup" element={<Signup />} />
          <Route path="/teacher-dashboard" element={<TeacherDashboard />} />
          <Route path="/student-dashboard" element={<StudentDashboard />} />
          <Route path="/teacher-answer-sheet" element={<TeacherAnswerSheet />} />
          <Route path="/student-answer-sheet/:subjectName" element={<StudentAnswerSheet />} />
          <Route path="/teacher-subject/:className" element={<TeacherSubjects />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;


