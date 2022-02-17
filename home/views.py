from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    context = {

    }
    # return HttpResponse('Successfully stored in  the database')
    return render(request, 'home/homePage.html', context)

def ProfessorHome(request):
    context = {

    }
    # return HttpResponse('Successfully stored in  the database')
    return render(request, 'home/Professor_Home.html', context)

def StudentHome(request):
    context = {

    }
    # return HttpResponse('Successfully stored in  the database')
    return render(request, 'home/Student_Home.html', context)

##############################################

from services.AMS import fitModel
from login.models import Subject
from django.contrib.auth.models import User

def trainModel(request):

    train_acc, test_acc = fitModel.main()

    context = {
        "train_acc": train_acc,
        "test_acc": test_acc
    }
    # return HttpResponse('Successfully stored in  the database')
    return render(request, 'home/trainModel.html', context)

from upload_Img import forms
from services.AMS import pred_Student
import pandas as pd

def mark_Attendance(request):
    name = False

    if request.method == 'POST':
        image = request.FILES.get('image')
        subjName = request.POST.get('subject')
        print(type(image))
        
        loginUser = str(request.user)
        name = pred_Student.predict(image, subjName, loginUser)
        
    context = {
        "name": name,
    }
    # return HttpResponse('Successfully stored in  the database')
    return render(request, 'upload_Img/mark_Attendance.html', context)