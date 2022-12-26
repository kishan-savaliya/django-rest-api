from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from .mypagination import MyCursorPagination

class StudentViewSet(viewsets.ModelViewSet):
    
    """viewset for student api view.

    Args:
        viewsets (_type_): _description_
    """

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyCursorPagination

