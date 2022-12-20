from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics,status

# Create your views here.

class AuthConfig(generics.GenericAPIView):
    def get(self,request):
        return Response(data={'message':'Hello Auth'},status=status.HTTP_200_OK)
