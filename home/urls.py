from django.contrib import admin
from django.urls import path
from home import views
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

urlpatterns = [
    path('home/', views.Home, name= 'home'),
    path('professor/home/', login_required(views.ProfessorHome), name= 'profHome'),
    path('student/home/', login_required(views.StudentHome) , name= 'stdHome'),

    path('fit/', views.trainModel, name= 'fit'),

    path('student/mark_Attendance', views.mark_Attendance, name= 'mark_Attendance'),
    # path('student/script.php', views.phpFile_Call),
]