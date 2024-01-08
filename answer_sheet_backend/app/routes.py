from flask import jsonify, request, session
from app import app, mongo
from app.models import Teacher, Student, Class_, Subject

# Example route
@app.route('/api/faltu', methods=['GET'])
def faltu():
    return "faltu fxn"

# Teacher login route
@app.route('/api/user/teacher/login', methods=['POST'])
def login_check():
    try:
        data = request.get_json()
        teacher = Teacher.find_one(data['user_name'], data['password'], mongo)

        if teacher:
            session['user_id'] = teacher.user_name
            return jsonify({'message': 'login successful'})
        else:
            return jsonify({'message': 'Teacher not found or invalid credentials'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Teacher registration route
@app.route('/api/user/teacher/register', methods=['POST'])
def register_check():
    try:
        data = request.get_json()
        teacher = Teacher.find_one(data['user_name'], data['password'], mongo)

        if teacher:
            return jsonify({'message': 'Teacher already exists, try another one'})
        else:
            new_teacher = Teacher(user_name=data['user_name'], password=data['password'])
            new_teacher.save_to_mongo(mongo)
            return jsonify({'message': 'Teacher registered successfully'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Student registration route
@app.route('/api/user/student/register', methods=['POST'])
def register_check_student():
    try:
        data = request.get_json()
        student = Student.find_one(data['user_name'], data['password'], mongo)

        if student:
            return jsonify({'message': 'Student already exists, try another one'})
        else:
            new_student = Student(user_name=data['user_name'], password=data['password'], class_name=data['class_name'])
            new_student.save_to_mongo(mongo)
            return jsonify({'message': 'Student registered successfully'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Student login route
@app.route('/api/user/student/login', methods=['POST'])
def login_check_student():
    try:
        data = request.get_json()
        student = Student.find_one(data['user_name'], data['password'], mongo)

        if student:
            return jsonify({'message': 'Student Login successfully', 'class_name': student.class_name})
        else:
            return jsonify({'message': 'Student not found or invalid credentials'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get class data
@app.route('/api/class_data', methods=['GET'])
def get_class_data():
    try:
        class_names = Class_.find_all(mongo)
        return jsonify([cls.__dict__ for cls in class_names])

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get student class
@app.route('/api/student_class', methods=['POST'])
def get_student_class():
    try:
        data = request.get_json()
        class_data = Class_.find_one(data['class_name'], mongo)

        if class_data:
            return jsonify({"class_name": class_data.class_name, "class_image": class_data.class_image})

        return None

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get teacher subjects
@app.route('/api/subject_data/<string:class_name>', methods=['GET'])
def get_teacher_subject(class_name):
    try:
        subjects = Subject.find_all_subjects(class_name, mongo)

        return jsonify(subjects)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get teacher answer sheets
@app.route('/api/answersheet/<string:class_name>/<string:subject_name>', methods=['GET'])
def get_teacher_answersheets(class_name, subject_name):
    try:
        answersheets = Subject.find_all_answersheets(class_name, subject_name, mongo)

        return jsonify({"answersheets": answersheets})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to add teacher answer sheets
@app.route('/api/answersheet_add/<string:class_name>/<string:subject_name>/<string:answersheet_name>', methods=['GET'])
def teacher_add_answersheets(class_name, subject_name, answersheet_name):
    try:
        answersheets = Subject.add_answersheet(class_name, subject_name, answersheet_name, mongo)

        return jsonify({"answersheets": answersheets})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to delete teacher answer sheets
@app.route('/api/answersheet_delete/<string:class_name>/<string:subject_name>/<string:answersheet_name>', methods=['GET'])
def teacher_delete_answersheets(class_name, subject_name, answersheet_name):
    try:
        answersheets = Subject.delete_answersheet(class_name, subject_name, answersheet_name, mongo)

        return jsonify({"answersheets": answersheets})

    except Exception as e:
        return jsonify({'error': str(e)}), 500



@app.route("/api/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        filename = photos.save(file)
        return jsonify({"message": "File uploaded successfully", "filename": filename})

    return jsonify({"error": "Invalid file type"}), 400

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ["jpg", "jpeg", "png"]

