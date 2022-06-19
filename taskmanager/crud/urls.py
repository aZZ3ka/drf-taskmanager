from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'todo', views.TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('todo/<int:id>/execute', views.TaskExecuteViewSet.as_view({'post': 'execute'}))
]
