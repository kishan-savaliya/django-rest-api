from django.contrib import admin
from .models import Singer, Song

@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    """register singer instances fields.

    Args:
        admin (_type_): _description_
    """
    list_display = ["id", "name", "gender"]

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    """register song instances fields.

    Args:
        admin (_type_): _description_
    """
    list_display = ["id", "title", "singer", "duration"]
