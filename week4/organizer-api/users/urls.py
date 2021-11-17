from django.urls import path, re_path, include
from . import views

app_name = "users"

urlpatterns = [
    path("register/", views.UserRegister.as_view(), name="register"),
    path("profile/", views.ProfileDetail.as_view(), name="user-profile"),
    path("", views.UserList.as_view(), name="users-list"),
    path("<uuid:pk>/", views.UserDetail.as_view(), name="user-detail"),
]
