from django.db import models
from .validators import validate_subject_format, validate_professor_name

class Subject(models.Model):
    subject_name = models.CharField(max_length=100, unique=True, validators=[validate_subject_format])
    professor = models.CharField(max_length=100, validators=[validate_professor_name])
    students = models.ManyToManyField('student_app.Student', related_name='Mysubjects')

    def __str__(self):
            return f"{self.subject_name} - {self.professor} - {self.students.count()}"

    def add_a_student(self, student_pk):
        if self.students.count() >= 31:
            raise Exception("This subject is full!")
        self.students.add(student_pk)

    def drop_a_student(self, student_pk):
        if self.students.count() <= 0:
            raise Exception("This subject is empty!")
        self.students.remove(student_pk)