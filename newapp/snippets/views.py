# from django.shortcuts import render
# from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework import renderers

# from rest_framework.views import APIView
from rest_framework.response import Response

# from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework import permissions
from rest_framework import generics
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from django.contrib.auth.models import User
from snippets.permissions import IsOwnerOrReadOnly


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "snippets": reverse("snippet-list", request=request, format=format),
            "users": reverse("user-list", request=request, format=format),
        }
    )


class SnippetList(generics.ListCreateAPIView):

    """
    list all snippets, create or new snippet using genericview.
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    authentication_classes = [BasicAuthentication]


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):

    """
    Retrive ,update, delete snippets using genericview.
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class SnippetList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)

# class SnippetDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)

#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)

#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)

# class SnippetList(APIView):

#     """
#     list all snippets, create or new snippet.
#     """

#     def get(self,request,format = None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets,many=True)
#         return Response(serializer.data)

#     def post(self,request,format = None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# class SnippetDetail(APIView):

#     """
#     Retrive ,update, delete snippets.
#     """

#     def get_object(self,pk):
#         try:
#             return Snippet.objects.get(pk = pk)
#         except Snippet.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def get(self,pk):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)

#     def put(self,request,pk):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     def delete(self,pk):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET','POST'])
# def snippet_list(request,format=None):

#     """
#     list all snippets, create or new snippet.
#     """

#     if request.method == 'GET':

#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets,many=True)

#         return Response(serializer.data)

#     elif request.method == 'POST':

#         serializer = SnippetSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()

#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET','PUT','DELETE'])
# def snippet_detail(request,pk,format=None):

#     """
#     Retrive ,update, delete snippets.
#     """

#     try:
#         Snippets = Snippet.objects.get(pk = pk)

#     except Snippet.DoesNotExist:

#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = SnippetSerializer(Snippets)

#         return Response(serializer.data)

#     elif request.method == 'PUT':

#         serializer = SnippetSerializer(Snippets,data=request.data)

#         if serializer.is_valid():
#             serializer.save()

#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         Snippets.delete()

#         return Response(status=status.HTTP_204_NO_CONTENT)
