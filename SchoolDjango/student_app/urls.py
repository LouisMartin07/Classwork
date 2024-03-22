from django.urls import path,register_converter
from .views import All_students,A_student
from .converters import IntOrStrConverter

register_converter(IntOrStrConverter, "int_or_str")

urlpatterns = [
    path("", All_students.as_view(), name='all_students'),
    path("<int_or_str:id>/", A_student.as_view(), name = 'a_students')
]