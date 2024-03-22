from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import StudentAllSerializer,StudentSerializer
# Create your views here.

class All_students(APIView):
    def get(self, request):
        students = Student.objects.all()
        serialized_students = StudentAllSerializer(students, many=True)
        return Response(serialized_students.data)
class A_student(APIView):

     def get(self, request, id): 
        pokemon = None
        if type(id) == int: 
            pokemon = Student.objects.get(id = id)
        else:
            pokemon = Student.objects.get(name = id.title()) 
        return Response(StudentSerializer(pokemon).data) 
    
