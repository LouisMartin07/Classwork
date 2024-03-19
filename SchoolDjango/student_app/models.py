from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255, blank=False)
    student_email = models.EmailField(unique=True, blank=False)
    personal_email = models.EmailField(unique=True, blank=True, null=True)
    locker_number = models.IntegerField(blank=False)
    locker_combination = models.CharField(max_length=10, blank=False)
    good_student = models.BooleanField(default=True)

