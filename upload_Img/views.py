"""
Refernces: https://www.geeksforgeeks.org/python-uploading-images-in-django/
"""
from django.http import HttpResponse
from django.shortcuts import render, redirect
from numpy import roll
from .forms import *
from upload_Img import models

from services.AMS import embedding
from django.core.files.base import ContentFile
from django.core.files import File
from PIL import Image

import time

# Create your views here.
def student_image_view(request):
    form = UploadImageForm(request.POST, request.FILES)  

    if request.method == 'POST':
        # This is required because it a file stored in ImageField of django db
            # print(form.instance.name)
            # print(form.instance.student_Img)
            # print(form.instance)
            # form.cleaned_data['subject'] subject is a variable name used in the model
        
        # roll_num = form.instance.Roll_Number
        roll_num = request.POST.get('Roll_Number')
        print(roll_num)
        # form.instance.student_Img.open()
        images = request.FILES.getlist('images')

        for img in images:
            print(type(img))
            # face_array = embedding.extract_face(form.instance.student_Img)
            # As One_face is numpy.ndarray, know by print(type(One_face))
            # We need to convert it into image which is bytes first
            # print(1, type(bytes(face_array)))
            # print(2, bytes(face_array))
            # face_image = ContentFile(bytes(face_array))
            # form.instance.student_Img = face_image  # This is not able to save the image in  the database
            # form.save()
            try:
                face_array = embedding.extract_face(img)
                vector_128 = embedding.face_embedding(face_array, roll_num)
            except:
                continue
            #To store faceImage
            # 1. Method- It save it in a form of bytes not readable as image by human
            # form.instance.student_Img.save('{0}.jpg'.format(form.instance.name), face_image, save=True)
            # 2. Method - Work
            # img = Image.fromarray(face_array)
            # img.save('{0}.jpg'.format(form.instance.name))

        # For Debugging
        # vector_128 is passed to a webpage to see the content or embedding extracted
        # context = {
        #     "vector_128": vector_128,
        #     "name": form.instance.name
        # }
        # return render(request, 'upload_Img/display_student_images.html', context)
        # return redirect('success')
        time.sleep(5)
        return redirect('/home/')
    else:
        form = UploadImageForm()
    return render(request, 'upload_Img/upload_Img.html', {'form' : form})
  
def success(request):
    return HttpResponse('Successfully stored in  the database')


def display_student_images(request):  
    if request.method == 'GET':
        # If we store the image in database then to display them on webpage
        # getting all the objects of hotel.
        stdImgs = Student_Images.objects.all() 
        context = {
            'std_images' : stdImgs
        }
        return render(request, 'upload_Img/display_student_images.html', context)
