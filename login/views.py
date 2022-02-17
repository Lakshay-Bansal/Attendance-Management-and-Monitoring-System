from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout

#Required to create the object in the User table of django
from django.contrib.auth.models import User
from django.contrib import messages
# from django.contrib.auth.hashers import make_password
# from passlib.hash import pbkdf2_sha256

from login import forms

# Create your views here.
def StudentLogin(request):
    error = None
    
    if request.method == "POST":
        # print(loginForm) For debug purpose
        rollnum = request.POST['Roll_Number']
        pasw = request.POST['Password']
        # print(rollnum, make_password(pasw) )
        user = authenticate(request, username = rollnum, password = pasw)
        print(user)
        if user:
            ## Before opening the page it authenticate the user
            auth_login(request, user)
            return redirect('/student/home/')
        else:
            error = "Invalid username or password"
      
    context = {
        "error": error
    } 
    # return HttpResponse('Successfully Login in AMS.')
    return render(request, 'login/std_Login.html', context)


def StudentSignUp(request):
    signUp = forms.Student_SignupForm(request.POST)
    message = None
    
    if request.method == "POST":
        if signUp.is_valid():
            name = signUp.instance.Name
            rollnum = signUp.instance.Roll_Number
            password = request.POST.get('pass1')
            print(rollnum)

            password_2 = request.POST.get('pass2')
            if password != password_2:
                message = "Passwords's didn't match."
            else:
                student = User.objects.create_user(username= rollnum, password= password)
                student.save()
                messages.success(request, "Your account has been created successfully.")

                signUp.save()
                message = "Your details are saved successfully."
                return render(request, 'login/std_Login.html')
        else:
            message = "Some fields are wrong. Please again fill the form."

    signUp =  forms.Student_SignupForm()        
    context = {
        "form": signUp,
        "message": message
    } 
    return render(request, 'login/std_Signup.html', context)


def ProfessorLogin(request):
    error = None
    
    if request.method == "POST":
        email = request.POST['email']
        pasw = request.POST['pass1']
        print(pasw)
        prof = authenticate(request, username = email, password = pasw)
        print(prof)
        if prof:
            error = None
            ## Before opening the page it authenticate the user
            auth_login(request, prof)
            return render(request, 'home/Professor_Home.html')
        else:
            error = "Invalid username or password"

    context = {
        "error": error
    }
    return render(request, 'login/prof_Login.html', context)


def ProfessorSignUp(request):
    signUp = forms.Prof_SignupForm(request.POST)
    message = None

    if request.method == "POST":
        if signUp.is_valid():
            # username = signUp.instance.Name
            email = signUp.instance.Email_ID
            password = request.POST.get('pass1')

            password_2 = request.POST.get('pass2')
            if password != password_2:
                message = "Passwords's didn't match."
            else:
                professor = User.objects.create_user(username = str(email), password = password) 
                professor.save()
                messages.success(request, "Your account has been created successfully.")

                signUp.save()
                message = "Your details are saved successfully."
                return render(request, 'login/prof_Login.html')
        else:
            message = "Some fields are wrong. Please again fill the form."
    
    signUp =  forms.Prof_SignupForm()        
    context = {
        "form": signUp,
        "message": message
    } 

    return render(request, 'login/prof_Signup.html', context)


def SignOut(request):
    logout(request)
    messages.success(request, "You are successfully logout")
    return render(request, 'login/logout.html')
