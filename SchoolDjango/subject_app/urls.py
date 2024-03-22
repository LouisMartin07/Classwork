from django.urls import path, register_converter
from .views import All_subjects,A_subject
from .converters import IntOrStrConverter

register_converter(IntOrStrConverter, "int_or_str")

urlpatterns = [
    path("", All_subjects.as_view(), name='all_subjects'),
    path('<int_or_str:id>/', A_subject.as_view(), name="a_subjects")
]