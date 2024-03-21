from django.db import models
from django.core import validators as v
from .validators import validate_name_format, validate_school_email,validate_combination_format

class Student(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=False, validators=[validate_name_format])
    student_email = models.EmailField(unique=True, blank=False, validators = [validate_school_email])
    personal_email = models.EmailField(unique=True, blank=True, null=True)
    locker_number = models.IntegerField(blank=False, unique=True, default=110, validators =[v.MinValueValidator(1), v.MaxValueValidator(200)])
    locker_combination = models.CharField(max_length=10, blank=False, unique=False, default="12-12-12", validators = [validate_combination_format])
    good_student = models.BooleanField(default=True)
    subjects = models.ManyToManyField('subject_app.Subject', related_name='Mystudents')


    def __str__(self):
        return f'{self.name} - {self.student_email} - {self.locker_number}'

    def locker_Change(self):
        self.locker_number = self.locker_number
        self.save()

    def status_change(self):
        self.good_student = not self.good_student
        self.save()

    def add_subject(self, subject_id):
            if self.subjects.count() >= 8:
                raise Exception("This student's class schedule is full!")
            self.subjects.add(subject_id)

    def remove_subject(self, subject_id):
        if self.subjects.count() <= 1:
            raise Exception("This student's class schedule is empty!")
        self.subjects.remove(subject_id)

    