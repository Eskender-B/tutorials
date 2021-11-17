from django.urls.conf import path, include
from rest_framework import routers, urlpatterns
from . import views

app_name = 'todo'

router = routers.DefaultRouter()

router.register('todo_lists', views.TODOListViewSet)
router.register('tasks', views.TaskViewSet)

urlpatterns = [
    path('', include(router.urls))
]

