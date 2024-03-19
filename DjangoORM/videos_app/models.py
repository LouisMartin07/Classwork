from django.db import models

class Client(models.Model):
    account_type = models.CharField()
    email = models.EmailField(unique=True)
    active = models.BooleanField(default=True)

class Video(models.Model):
    title = models.CharField(max_length=255)
    in_stock = models.BooleanField(default=True)
    rating = models.IntegerField(null=True, blank=True)

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_init = models.CharField(max_length=1, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)

class Address(models.Model):
    street = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=10)  
    state = models.CharField(max_length=100)
    appt_num = models.IntegerField(null=True, blank=True)

class Store(models.Model):  
    name = models.CharField(max_length=255)
    number_of_employees = models.IntegerField()
    rating = models.IntegerField(null=True, blank=True) 
    owner = models.CharField(max_length=100)