from django.urls import path
from snippets import views
from snippets.auth import CustomAuthToken
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("snippets/", views.SnippetList.as_view(), name="snippet-list"),
    path("snippets/<int:pk>/", views.SnippetDetail.as_view(), name="snippet-list"),
    path("users/", views.UserList.as_view(), name="user-list"),
    path("users/<int:pk>/", views.UserDetail.as_view(), name="user-list"),
    path("auth-token/", CustomAuthToken.as_view()),
    path("", views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
