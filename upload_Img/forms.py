from django import forms
from .models import *
  
class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Student_Images
        fields = "__all__"