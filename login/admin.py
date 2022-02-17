from django.contrib import admin

from login import models

# Register your models here.
admin.site.register({
    models.Subject,
    models.Student_Signup_Form,
    models.Prof_Signup_Form,
})


