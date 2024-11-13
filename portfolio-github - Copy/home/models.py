from django.db import models

# Create your models here.
#ORM - 

class info(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(null=False)
    birthday = models.DateField(null=False)
    gender = models.CharField(null=False, max_length=200)
    phone = models.CharField(null=False, max_length=20)
    email = models.EmailField(null=False)
    address = models.CharField(null=True, max_length=200)
    schools = models.CharField(max_length=200)

    def __str__(self):
        return self.name