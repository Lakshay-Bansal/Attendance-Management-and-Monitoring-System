from django.contrib import admin
from django.urls import path
from login import views

urlpatterns = [
    path('professor/login/', views.ProfessorLogin, name= 'profLogin'),
    path('student/login/', views.StudentLogin , name= 'stdLogin'),
    path('professor/signUp/', views.ProfessorSignUp, name= 'profsignUp'),
    path('student/signUp/', views.StudentSignUp , name= 'stdsignUp'),   

    # path('home/', views.ProfessorSignOut, name= 'profsignOut'),
    # path('home/', views.StudentSignOut, name= 'stdsignOut'),
    path('logout/', views.SignOut, name='signout')
]