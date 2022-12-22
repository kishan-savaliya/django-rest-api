from django.urls import path
from . import views

urlpatterns = [
    path('', views.AuthConfig.as_view(),name='hello auth'),
]
