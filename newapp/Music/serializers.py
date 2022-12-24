from .models import Singer,Song
from rest_framework import serializers

class SingerSerializer(serializers.ModelSerializer):
    song = serializers.StringRelatedField(many=True, read_only = True)
    # song = serializers.PrimaryKeyRelatedField(many=True, read_only = True)
    # song = serializers.HyperlinkedRelatedField(view_name='song-detail', many=True, read_only = True)

    class Meta:
        model = Singer
        fields = ['id','name','gender','song']

class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ['id','singer','title','duration']
