from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Grade
from .serializers import GradeSerializer

class AGrade(APIView):

    def put(self, request, pk):
        grade = Grade.objects.get(pk=pk)
        serializer = GradeSerializer(grade, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def post(sef,request):
        new_grade = GradeSerializer(data=request.data)
        if new_grade.is_valid():
            new_grade.save()
            return Response(new_grade.data, status = status.HTTP_201_CREATED)


    def delete(self,request,pk):
        grade = Grade.objects.get(pk=pk)
        grade.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)