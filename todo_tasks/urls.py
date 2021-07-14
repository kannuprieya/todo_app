from django.urls import path
from django.shortcuts import reverse
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', login_required(views.TaskListView.as_view(), login_url='login'), name='intro'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('add_task/', login_required(views.TaskCreateView.as_view(), login_url='login'), name="add_task"),
    path('add_task/thank_you/', views.thank_you, name= 'thanks'),
    path('task_delete/<int:pk>/', login_required(views.TaskDeleteView.as_view(), login_url='login'), name='task_delete'),
    path('task_update/<int:pk>/', login_required(views.TaskUpdateView.as_view(), login_url='login'), name='task_update'),
]
