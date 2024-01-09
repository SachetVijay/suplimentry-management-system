# suplimentry-management-systemAnswer Sheet Platform

Overview

The Answer Sheet Platform is a web application built with ReactJS for the frontend and Flask for the backend. It serves as a platform for teachers and students, providing efficient management and access to answer sheets. Key features include class and subject management, bulk and individual answer sheet uploads, automatic mapping logic, and secure viewing/download capabilities.

Setup

Frontend
Navigate to Frontend Directory:
cd frontend
Install Dependencies:
npm install
Start Development Server:
npm start
The application is accessible at http://localhost:3000.
Backend
Navigate to Backend Directory:
cd answer_sheet_backend
Install Python Dependencies:
pip install -r requirements.txt
Run Flask Application:
python run.py
The backend is running at http://127.0.0.1:5000.
Project Structure

The project is organized into the following components:

frontend: ReactJS-based user interface.
backend: Flask-based backend server handling server-side functionalities.

Features

Teacher's Interface
Class and Subject Management
Answer Sheet Uploads
Deletion Capability
Answer Sheet Viewing
Student's Interface
Subject Dashboard
Restricted Access to Own Answer Sheets
Usage

Student Dashboard
Upon logging in as a student, you'll be directed to the Student Dashboard.
The dashboard displays your classes, and upon clicking, it leads you to subject-specific answer sheets.
Teacher Dashboard
Upon logging in as a teacher, you'll be directed to the Teacher Dashboard.
The dashboard displays subjects for the selected class, allowing you to manage and view answer sheets.
Answer Sheet Pages
Both teachers and students can view answer sheets. Students only have access to their own answer sheets.
Adding/Deleting Answer Sheets (Teacher Only)
Teachers can add new answer sheets and delete existing ones from the Teacher Answer Sheet page.
Dockerization

Dockerfile
A Dockerfile is provided to build the Docker image for the application.
