from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    number_of_pets = models.IntegerField(default=0) 

class Cat(models.Model):
    breed = models.CharField(max_length=50)
    age = models.IntegerField()
    vaccinated = models.BooleanField()
    description = models.TextField(blank=True, null=True) 
    name = models.CharField(max_length=50)

class Bird(models.Model):
    species = models.CharField(max_length=50)
    age = models.IntegerField()
    vaccinated = models.BooleanField()
    description = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=50)

class Dog(models.Model):
    breed = models.CharField(max_length=50)
    age = models.IntegerField()
    vaccinated = models.BooleanField()
    description = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=50)

class Exotic_Animal(models.Model):
    region_of_origin = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    type_of_animal = models.CharField(max_length=50)
    vaccinated = models.BooleanField()