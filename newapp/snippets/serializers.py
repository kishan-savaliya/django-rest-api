from rest_framework import serializers
from snippets.models import Snippet
from django.contrib.auth.models import User


class SnippetSerializer(serializers.ModelSerializer):

    """
    create and return new 'snippet' instance, given the validated data. 
    """

    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:

        model = Snippet
        fields = ["id", "title", "code", "linenos", "language", "owner"]


class UserSerializer(serializers.ModelSerializer):

    """
    create and return new 'user' instance, given the validated data. 
    """

    snippets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Snippet.objects.all()
    )

    class Meta:

        model = User
        fields = ["id", "username", "snippets"]


# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     title = serializers.CharField(required = False,allow_blank = True,max_length = 100)
#     code = serializers.CharField(style={'base_template':'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

# def create(self,validated_data):

#     """
#     create and return new 'snippet' instance, given the validated data.
#     """
#     return Snippet.objects.create(**validated_data)

# def update(self,instance,validated_data):

#     """
#     update and return existing 'snippet' instance, given the validated data.
#     """
#     instance.title = validated_data.get('title',instance.title)
#     instance.code = validated_data.get('code',instance.code)
#     instance.lineous = validated_data.get('lineous',instance.lineous)

#     instance.save()

#     return instance
