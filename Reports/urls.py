from django.contrib import admin
from django.urls import path
from Reports import views

urlpatterns = [
    path('student/report', views.stdReport, name= 'stdReport'),
    path('professor/report', views.profReport, name= 'profReport'),
]