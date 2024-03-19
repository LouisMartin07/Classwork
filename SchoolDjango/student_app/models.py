from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=False)
    student_email = models.EmailField(unique=True, blank=False)
    personal_email = models.EmailField(unique=True, blank=True, null=True)
    locker_number = models.IntegerField(blank=False, unique=True, default=110)
    locker_combination = models.CharField(max_length=10, blank=False, unique=False, default="12-12-12")
    good_student = models.BooleanField(default=True)

def __str__(self):
    return f'{self.name} - {self.student_email} - {self.locker_number}'

def locker_Change(self):
    self.locker_number = self.locker_number
    self.save()

def status_change(self):
    self.good_student = not self.good_student
    self.save()