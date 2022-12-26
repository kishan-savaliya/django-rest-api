from django.db import models

class Singer(models.Model):
    
    """create model for singer instances.

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """

    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Song(models.Model):

    """create model for song instances.

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """

    title = models.CharField(max_length=100)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name="song")
    duration = models.IntegerField()

    def __str__(self):
        return self.title
