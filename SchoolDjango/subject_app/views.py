from django.shortcuts import render
from .serializers import Subject, SubjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class All_subjects(APIView):
    def get(self, request):
        subjects = Subject.objects.all()
        serialized_subjects = SubjectSerializer(subjects, many=True)
        return Response(serialized_subjects.data)


class A_subject(APIView):

     def get(self, request, id): 
        pokemon = None
        if type(id) == int: 
            pokemon = Subject.objects.get(id = id)
        else:
            pokemon = Subject.objects.get(name = id.title()) 
        return Response(SubjectSerializer(pokemon).data) 


