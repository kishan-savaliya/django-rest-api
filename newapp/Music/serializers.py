from .models import Singer, Song
from rest_framework import serializers

class SingerSerializer(serializers.ModelSerializer):

    """
    create and return new 'singer' instance, given the validated data.
    """

    song = serializers.StringRelatedField(many=True, read_only=True)
    # song = serializers.PrimaryKeyRelatedField(many=True, read_only = True)
    # song = serializers.HyperlinkedRelatedField(view_name='song-detail', many=True, read_only = True)

    class Meta:
        model = Singer
        fields = ["id", "name", "gender", "song"]

class SongSerializer(serializers.ModelSerializer):

    """
    create and return new 'song' instance, given the validated data.
    """

    class Meta:
        model = Song
        fields = ["id", "singer", "title", "duration"]
