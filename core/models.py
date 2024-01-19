from django.db import models

# Create your models here.
class Application(models.Model):
    First_Name = models.CharField(max_length=25)
    Last_Name = models.CharField(max_length=25)
    LinkedIn = models.URLField()
    Email = models.EmailField()
    Phone_Num = models.IntegerField()
    Text = models.CharField(max_length=10000)
    resume = models.FileField(upload_to='resumes/')