from django.db import models

# Create your models here.
class Student_Images(models.Model):
    Roll_Number = models.CharField(max_length=50)
    # Surprised_Img_1 = models.ImageField(blank=True, null = True, upload_to='images/')
    # Surprised_Img_2 = models.ImageField(upload_to='images/')
    # Angry_Img_1 = models.ImageField(upload_to='images/')
    # Angry_Img_2 = models.ImageField(upload_to='images/')
    # Smile_Img_1 = models.ImageField(upload_to='images/')
    # Smile_Img_2 = models.ImageField(upload_to='images/')
    # Sad_Img_1 = models.ImageField(upload_to='images/')
    # Sad_Img_2 = models.ImageField(upload_to='images/')
    # Different_Pose_Img_1 = models.ImageField(upload_to='images/')
    # Different_Pose_Img_2 = models.ImageField(upload_to='images/')
    Face_Images = models.ImageField(null=True, blank=True, upload_to='images/')

    # student_Img = models.ImageField(upload_to='images/{0}.jpg'.format(name) )
    def __str__(self):
        return self.Roll_Number