# from flask_cors import CORS
# from pymongo import MongoClient
# from pymongo.server_api import ServerApi
# import gridfs



# from flask import Flask, jsonify, request, session, redirect, url_for
# from flask_pymongo import PyMongo
# from .models import Teacher, Student, Class_, Subject

# app = Flask(__name__)
# CORS(app, resources={r"/api/*": {"origins": "*", "supports_credentials": True, "expose_headers": "Set-Cookie"}})

# app.config["MONGO_URI"] = "mongodb+srv://ui20cs61:Sachet123@cluster0.pl1zog4.mongodb.net/db?retryWrites=true&w=majority"
# app.config["SECRET_KEY"] = "93f9b1c66ebed8edb26c18a4af41f65c1f7131df0878a497460e39dbca2c69c7"
# app.config['SESSION_COOKIE_SECURE'] = True
# app.config['SESSION_DEBUG'] = True

# mongo = PyMongo(app)
# print(mongo)
# # Your MongoDB connection setup
# uri = "mongodb+srv://ui20cs61:Sachet123@cluster0.pl1zog4.mongodb.net/db?retryWrites=true&w=majority"
# client = MongoClient(uri, server_api=ServerApi('1'))

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)


# @app.route('/api/faltu', methods=['GET'])
# def faltu():
#     return "faltu fxn"

# @app.route('/api/user/teacher/login', methods=['POST'])
# def login_check():
#     try:
#         data = request.get_json()
#         teacher = Teacher.find_one(data['user_name'], data['password'], mongo)
#         print(teacher)

#         if teacher:
#             session['user_id'] = teacher.user_name
#             return ('login successful!')
#         else:
#             return jsonify({'message': 'Teacher not found or invalid credentials'}), 404

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# # teacher register route.....complete
# @app.route('/api/user/teacher/register', methods=['POST'])
# def register_check():
#     try:
#         data = request.get_json()
#         teacher = Teacher.find_one(data['user_name'], data['password'], mongo)
#         print(teacher)
#         if teacher:
#             return jsonify({'message': 'Teacher already exists, try another one'})
#         else:
#             new_teacher = Teacher(user_name=data['user_name'], password=data['password'])
#             new_teacher.save_to_mongo(mongo)
#             return jsonify({'message': 'Teacher registered successfully'})

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# # student register route
# @app.route('/api/user/student/register', methods=['POST'])
# def register_check_student():
#     try:
#         data = request.get_json()
#         student = Student.find_one(data['user_name'], data['password'], mongo)
        
#         if student:
#             return jsonify({'message': 'Student already exists, try another one'})
#         else:
#             new_student = Student(user_name=data['user_name'], password=data['password'], class_name=data['class_name'])
#             # print(new_student.user_name)
#             new_student.save_to_mongo(mongo)
#             return jsonify({'message': 'Student registered successfully'})

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# @app.route('/api/user/student/login', methods=['POST'])
# def login_check_student():
#     try:
#         # print('hello student logged in')
#         data = request.get_json()
#         # print (data)
#         # print('hehe')
#         student = Student.find_one(data['user_name'], data['password'], mongo)
#         # print(student)

#         if student:
#             # session['user_id'] = student.user_name
#             # print(student.class_name)
#             return jsonify({'message': 'Student Login successfully', 'class_name' : student.class_name})
#         else:
#             return jsonify({'message': 'Student not found or invalid credentials'}), 404

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# @app.route('/api/class_data', methods=['GET'])
# def get_class_data():
#     try:
#         # print('hello')
#         class_names = Class_.find_all(mongo)
#         print(class_names)
        
#         return class_names

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500
    
# @app.route('/api/student_class', methods=['POST'])
# def get_student_class():
#     try:
#         data = request.get_json()
#         print(data)
#         class_data = Class_.find_one(data['class_name'], mongo)
#         # print(class_data.class_name)
        
#         if class_data:
#             return jsonify({"class_name":class_data.class_name, "class_image":class_data.class_image})
        
#         return None
        

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500
    
    
# @app.route('/api/subject_data/<string:class_name>', methods=['GET'])
# def get_teacher_subject(class_name):
#     try:
#         # You can now use the class_name variable in your code
#         print("Class Name:", class_name)

#         # Assuming you have a method to find the class data based on the class name
#         subjects = Subject.find_all_subjects(class_name, mongo)
#         print(subjects)
#         # if subjects:
#         #         subject_list = [{
#         #         "subject_name": subject.subject_name,
#         #         "subject_image": subject.subject_image
#         #     } for subject in subjects]


#         return subjects
    
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

    
# @app.route('/api/answersheet/<string:class_name>/<string:subject_name>', methods=['GET'])
# def get_teacher_answersheets(class_name, subject_name):
#     try:
#         # You can now use the class_name variable in your code
#         print("Class Name:", class_name)
#         print("Subject Name:", subject_name)
#         # Assuming you have a method to find the class data based on the class name
#         answersheets = Subject.find_all_answersheets(class_name, subject_name, mongo)
#         print(answersheets)
#         # if subjects:
#         #         subject_list = [{
#         #         "subject_name": subject.subject_name,
#         #         "subject_image": subject.subject_image
#         #     } for subject in subjects]
#         return answersheets
    
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500
    
   
# @app.route('/api/answersheet_add/<string:class_name>/<string:subject_name>/<string:answersheet_name>', methods=['GET'])
# def teacher_add_answersheets(class_name, subject_name, answersheet_name):
#     try:
#         # You can now use the class_name variable in your code
#         print("Class Name:", class_name)
#         print("Subject Name:", subject_name)
#         print("AnswerSheet Name:", answersheet_name)
#         # Assuming you have a method to find the class data based on the class name
#         answersheets = Subject.add_answersheet(class_name, subject_name, answersheet_name, mongo)
#         print(answersheets)
#         return answersheets
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500
    

# @app.route('/api/answersheet_delete/<string:class_name>/<string:subject_name>/<string:answersheet_name>', methods=['GET'])
# def teacher_delete_answersheets(class_name, subject_name, answersheet_name):
#     try:
#         # You can now use the class_name variable in your code
#         print("Class Name:", class_name)
#         print("Subject Name:", subject_name)
#         print("AnswerSheet Name:", answersheet_name)
#         # Assuming you have a method to find the class data based on the class name
#         answersheets = Subject.delete_answersheet(class_name, subject_name, answersheet_name, mongo)
#         print(answersheets)
#         return answersheets
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)



from flask_cors import CORS
from flask import Flask, jsonify, request, session, redirect, url_for
from flask_pymongo import PyMongo
from flask_uploads import UploadSet, configure_uploads, IMAGES
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from .models import Teacher, Student, Class_, Subject

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*", "supports_credentials": True, "expose_headers": "Set-Cookie"}})

# Your MongoDB connection setup
uri = "mongodb+srv://ui20cs61:Sachet123@cluster0.pl1zog4.mongodb.net/db?retryWrites=true&w=majority"
app.config["MONGO_URI"] = uri
app.config["SECRET_KEY"] = "93f9b1c66ebed8edb26c18a4af41f65c1f7131df0878a497460e39dbca2c69c7"
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_DEBUG'] = True
app.config['UPLOAD_FOLDER'] = 'static/uploads'

photos = UploadSet("photos", IMAGES)
configure_uploads(app, photos)


mongo = PyMongo(app)
print(mongo)

client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Import routes after initializing Flask app and MongoDB
from .routes import *






