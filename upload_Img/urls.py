from django.contrib import admin
from django.urls import path
from upload_Img import views

urlpatterns = [
    path('upload/', views.student_image_view, name = 'upload'),

    #For Debugging Purpose
    path('success/', views.success, name = 'success'),
    path('std_images/', views.display_student_images, name = 'std_images'),
]    
  
#To handle the media folder
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)