from flask import Flask, jsonify, request,session, redirect
# from passlib.hash import pbkdf2_sha256



# class Teacher:
#     def __init__(self, user_name, password):
#         self.user_name = user_name
#         self.password = password


from passlib.hash import pbkdf2_sha256
from flask_pymongo import PyMongo

class Student:
    def __init__(self, user_name, password, class_name):
        self.user_name = user_name
        self.password = password
        self.class_name = class_name
        
    @staticmethod
    def find_one(username, password, mongo):
        # print(mongo)
        student_collection = mongo.db.students
        # print(username)
        # print(password)
        student_data = student_collection.find_one({"user_name": username})
        # print(student_data)
        if student_data:
            return Student(user_name=student_data['user_name'], password=student_data['password'], class_name=student_data['class_name'])
        return None
    
    def find_student(username, mongo):
        # print(mongo)
        student_collection = mongo.db.students
        # print(username)
        # print(password)
        print("in the find_student function")
        student_data = student_collection.find_one({"user_name": username})
        # print('hello')
        print("thissss")
        print(student_data)
        if student_data:
            return student_data['class_name']
        return None

    def save_to_mongo(self, mongo):
        student_data = {
            "user_name": self.user_name,
            "password": self.password,
            "class_name": self.class_name
        }
        mongo.db.students.insert_one(student_data)
 
class Subject:
    def __init__(self, subject_name, class_name, subject_image, students, answersheets):
        self.subject_name = subject_name
        self.class_name = class_name
        self.subject_image = subject_image
        self.students = students
        self.answersheets = answersheets
    
    @staticmethod
    
    def find_one(class_name, mongo):
        subject_collection = mongo.db.subject
        
        subject_data = subject_collection.find({"class_name": class_name})
        
        if subject_data:
            return {
                "subject_name": subject_data.get("subject_name", ""),
                "subject_image": subject_data.get("subject_image", "")
            }
        return None
    
    def find_all_subjects(class_name, mongo):
        subject_collection = mongo.db.subject
        print("entry")
        subject_data = subject_collection.find({"class_name": class_name})
        subject_data = list(subject_data)
        print(subject_data)
        subject_list = []
        for subject_entry in subject_data:
            subject_list.append({
                "subject_name": subject_entry.get("subject_name", ""),
                "subject_image": subject_entry.get("subject_image", "")
            })
        print(subject_list)
        if subject_list:
            return jsonify(subject_list)
        # print('hello')
        
        return None
    
    
    def find_all_answersheets(class_name, subject_name, mongo):
        subject_collection = mongo.db.subject
        # print("entry")
        subject_data = subject_collection.find_one({"class_name": class_name, "subject_name": subject_name})
        if subject_data:
            answersheets = subject_data.get("answersheets", [])
        return jsonify({"answersheets": answersheets})
    
    def add_answersheet(class_name, subject_name, answersheet_name, mongo):
        try:
            subject_collection = mongo.db.subject
            # print("entry")
            subject_data = subject_collection.find_one({"class_name": class_name, "subject_name": subject_name})
            if subject_data:
                # Assuming "answersheets" is the key for the array in the subject_data
                answersheets = subject_data.get("answersheets", [])
                answersheets.append(answersheet_name)

                # Update the subject_data with the new answersheets array
                subject_collection.update_one(
                    {"class_name": class_name, "subject_name": subject_name},
                    {"$set": {"answersheets": answersheets}}
                )

                return jsonify({"answersheets": answersheets})

            return jsonify({"error": "Subject not found"}), 404

        except Exception as e:
            return jsonify({'error': str(e)}), 500
        
        
    def delete_answersheet(class_name, subject_name, answersheet_name, mongo):
        try:
            subject_collection = mongo.db.subject
            # print("entry")
            subject_data = subject_collection.find_one({"class_name": class_name, "subject_name": subject_name})
            if subject_data:
                # Assuming "answersheets" is the key for the array in the subject_data
                answersheets = subject_data.get("answersheets", [])

                # Check if the answersheet_name exists in the array
                if answersheet_name in answersheets:
                    # Remove the answersheet_name from the answersheets array
                    answersheets.remove(answersheet_name)

                    # Update the subject_data with the modified answersheets array
                    subject_collection.update_one(
                        {"class_name": class_name, "subject_name": subject_name},
                        {"$set": {"answersheets": answersheets}}
                    )

                    return jsonify({"answersheets": answersheets})

            return jsonify({"error": "Answersheet not found in subject"}), 404

        except Exception as e:
           return jsonify({'error': str(e)}), 500

        
class Class_:
    def __init__(self, class_name, class_image):
        self.class_name = class_name
        self.class_image = class_image
        
    @staticmethod
    
    def find_one(class_name, mongo):
        class_collection = mongo.db.classes
        
        class_data = class_collection.find_one({"class_name": class_name})
        
        if class_data:
            return Class_(class_name=class_data['class_name'], class_image=class_data['class_image'])
        return None
    
    def find_all(mongo):
        print(mongo)
        class_collection = mongo.db.classes
        print(class_collection)
        # print(username)
        # print(password)
        class_data = class_collection.find({})
        # class_data = list(class_data)
        class_list = []
        for class_entry in class_data:
            class_list.append(Class_(
                class_name=class_entry['class_name'],
                class_image=class_entry['class_image']
            ))

        if class_list:
            return jsonify([cls.__dict__ for cls in class_list])
        # print('hello')
        
        return None

    # def save_to_mongo(self, mongo):
    #     student_data = {
    #         "user_name": self.user_name,
    #         "password": self.password,
    #         "class_name": self.class_name
    #     }
    #     mongo.db.students.insert_one(student_data)


# class AnswerSheet:
#     def __init__(self, subject, student_name, file_path):
#         self.subject = subject
#         self.student_name = student_name
#         self.file_path = file_path

# # Additional models as needed


# mongo = PyMongo()

class Teacher:
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = pbkdf2_sha256.hash(password)

    @staticmethod
    def find_one(username, password, mongo):
        # print(mongo)
        teachers_collection = mongo.db.teachers
        # print(username)
        # print(password)
        teacher_data = teachers_collection.find_one({"user_name": username})
        # print('hello')
        if teacher_data:
            return Teacher(user_name=teacher_data['user_name'], password=teacher_data['password'])
        return None

    def save_to_mongo(self, mongo):
        teacher_data = {
            "user_name": self.user_name,
            "password": self.password
        }
        mongo.db.teachers.insert_one(teacher_data)
