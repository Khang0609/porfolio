from django.db import models

# Create your models here.
class Infor(models.Model):
    name  = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    birth = models.DateField()
    email = models.EmailField()
    residence = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    facebook = models.URLField()
    logo = models.CharField(max_length=20)
    call_description = models.TextField()
    hobby1 = models.CharField(max_length=250)
    hobby1_description = models.TextField()
    hobby2 = models.CharField(max_length=250)
    hobby2_description = models.TextField()
    hobby3 = models.CharField(max_length=250)
    hobby3_description = models.TextField()
    work1 = models.CharField(max_length=250)
    work1_description = models.TextField()
    work2 = models.CharField(max_length=250)
    work2_description = models.TextField()
    work3 = models.CharField(max_length=250)
    work3_description = models.TextField()
    work1_img = models.ImageField(upload_to='images/')
    work2_img = models.ImageField(upload_to='images/')
    work3_img = models.ImageField(upload_to='images/')
    about_description = models.TextField()