from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.HyperlinkedModelSerializer):

    """serializer class of student instances.

    Args:
        serializers (_type_): _description_
    """
    
    class Meta:
        model = Student
        fields = ['id','url','name','roll','city']