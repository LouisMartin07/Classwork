from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lmartin@localhost/school'

db = SQLAlchemy(app)

class Student(db.Model):
    StudentID = db.Column(db.integer, primary_key=True)
    FirstName = db.Column(db.string(100))
    LastName = db.Column(db.string(100))
    Age = db.Column(db.integer(3))
    Class = db.Column(db.string(100))

class Teacher(db.Model):
    TeacherID = db.Column(db.integer, primary_key=True)
    FirstName = db.Column(db.string(100))
    LastName = db.Column(db.string(100))
    Age = db.Column(db.integer(3))
    Class = db.Column(db.string(100))

class Subject(db.Model):
    SubjectID = db.Column(db.integer, primary_key=True) 
    SubjectName = db.Column(db.string(100))

@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    teachers = Teacher.query.all()
    subjects = Subject.query.all()

    subjects_dict = {subject.subject_id: subject.subject_name for subject in subjects}

    teachers_dict = {}
    for teacher in teachers:
        if teacher.subject_id not in teachers_dict:
            teachers_dict[teacher.subject_id] = f"{teacher.first_name} {teacher.last_name}"

    students_data = []
    for student in students:
        subject_name = subjects_dict.get(student.subject_id, "Unknown Subject")
        teacher_name = teachers_dict.get(student.subject_id, "Unknown Teacher")

        students_data.append({
            "id": student.student_id,
            "first_name": student.first_name,
            "last_name": student.last_name,
            "age": student.age,
            "class": {
                "subject": subject_name,
                "teacher": teacher_name
            }
        })
    
    return jsonify(students_data)

app.run(debug=True)