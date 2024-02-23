from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lmartin@localhost/students'

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    grade = db.Column(db.String(1))

app.route('/old_students/', methods = ['GET'])
def old_students():
    pass
app.route('/young_students/', methods = ['GET'])
def young_students():
    pass

app.route('/advance_students/', methods = ['GET'])
def advance_students():
    pass

app.route('/student_names/', methods = ['GET'])
def student_names():
    pass

app.route('/student_ages/', methods = ['GET'])
def get_student_ages():
    pass

@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    student_list = [
        {'id': student.id, 'first_name': student.first_name, 'last_name': student.last_name, 'age': student.age, 'grade': student.grade}
        for student in students
    ]
    return jsonify(student_list)        


app.run(debug=True)