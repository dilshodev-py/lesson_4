from django.urls import path
from apps.views import TaskListView, TaskDetailView, TaskFormView, TaskDeleteView

urlpatterns = [
    path('task-list' , TaskListView.as_view(), name='task-list'),
    path('task-detail/<int:pk>' , TaskDetailView.as_view(), name='task-detail'),
    path('task-form' , TaskFormView.as_view(), name='task-form'),
    path('task-list/<int:pk>' , TaskDeleteView.as_view(), name='task_delete'),
]
