from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("users/", include("users.urls", namespace="users")),
    path("", include("todo.urls", namespace="todo")),
    path("auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("auth/token/", obtain_auth_token),
]
