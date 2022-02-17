from django.db import models

from django.core.validators import (
    EmailValidator,
)    

from django.core.exceptions import ValidationError

def email_checker(email):
    if "@iitm.ac.in" not in email:
        raise ValidationError("Please check your email address again.")

# Create your models here.
class Subject(models.Model):
    subjectName = models.CharField(max_length=100, blank=False, null=False)
    
    def __str__(self):
        return self.subjectName



class Student_Signup_Form(models.Model):
    COURSES = (
        ('b', 'B.Tech'),
        ('m', 'M.tech/MS'),
        ('p', 'PhD')
    )
    GENDERS = (
        ('f', 'Female'),
        ('m', 'Male'),
        ('u', 'Undisclosed')
    )
    SCHOOL = (
        ('c', 'SCEE'),
        ('b', 'SBS'),
        ('e', 'SE'),
        ('h', 'SHSS')
    )
    Name = models.CharField(max_length=50, blank=False, null=False)
    Roll_Number = models.CharField(primary_key = True, max_length=6, blank=False, null=False)
    Gender = models.CharField(max_length=1, choices=GENDERS, blank=False, null=False)
    School = models.CharField(max_length=1, choices=SCHOOL, blank=False, null=False)
    Course = models.CharField(max_length=1, choices=COURSES, blank=False, null=False)
    Branch = models.CharField(max_length=50, blank=False, null=False)

    Subjects = models.ManyToManyField('Subject')
    # Subject_2 = models.ManyToManyField('Subject')
    # Subject_3 = models.ManyToManyField('Subject')
    # Subject_4 = models.ManyToManyField('Subject')
    # Subject_5 = models.ManyToManyField('Subject')
    # Subject_6 = models.ManyToManyField('Subject')
    
    def __str__(self):
        return "{}-{}-{}".format(self.Roll_Number, self.Course, self.Branch)



class Prof_Signup_Form(models.Model):
    DESIGNATION = (
        ('a', "Assistant Professor"),
        ('A', "Associate Professor"),
        ('p', "Professor")
    )
    SCHOOL = (
        ('c', 'SCEE'),
        ('b', 'SBS'),
        ('e', 'SE'),
        ('h', 'SHSS')
    )
    Name = models.CharField(max_length=50, blank=False, null=False)

    Email_ID = models.CharField(
        primary_key = True,
        max_length=50, 
        validators=[
            EmailValidator(message="Please check your email again"),
            
            email_checker
        ],
        null=False 
    )
    Designation = models.CharField(max_length=1, choices=DESIGNATION, blank=False, null=False)
    School = models.CharField(max_length=1, choices=SCHOOL, blank=False, null=False)

    Offering_Courses = models.ManyToManyField('Subject')
    # Course_Offered_2 = models.ManyToManyField('Subject')
    # Course_Offered_3 = models.ManyToManyField('Subject')
    # Course_Offered_4 = models.ManyToManyField('Subject')

    def __str__(self):
        return "{}-{}-{}".format(self.Name, self.School, self.Designation)
