from django.db import models

class Student(models.Model):

    """models for student instances. 

    Args:
        models (_type_): _description_
    """
    
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)

