from django.shortcuts import render
from .models import Singer,Song
from .serializers import SingerSerializer,SongSerializer
from rest_framework import viewsets
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .mypagination import ResultSetPagination
from rest_framework.pagination import PageNumberPagination

class SingerViewSet(viewsets.ModelViewSet):

    """
    viewset of singer class 
    """
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    pagination_class = ResultSetPagination

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name','gender']

    # filter_backends = [filters.SearchFilter]
    # search_fields = ['name','gender']
    # throttle_classes = [AnonRateThrottle,UserRateThrottle]
    # authentication_classes = [JWTAuthentication]

class SongViewSet(viewsets.ModelViewSet):

    """
    viewset of song class
    """

    queryset = Song.objects.all()
    serializer_class = SongSerializer

    # throttle_classes = [AnonRateThrottle,UserRateThrottle]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    pagination_class = ResultSetPagination
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['id','title']

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','singer']