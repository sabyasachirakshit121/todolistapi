from django.urls import path
from . import views
urlpatterns = [
    path('api/', views.apiOverview, name="api-overview"),
    path('task-list/', views.taskList, name="task-list"),
]
