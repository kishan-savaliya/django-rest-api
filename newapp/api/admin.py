from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    """register student instances.

    Args:
        admin (_type_): _description_
    """
    
    list_display = ['id','name','roll','city']