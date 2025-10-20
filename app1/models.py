from django.db import models

# Create your models here.
class Stundents(models.Model):
    srollno=models.CharField(max_length=10)
    sname=models.CharField(max_length=64)
    sphoneno=models.IntegerField()
    sm1=models.IntegerField()
    sm2=models.IntegerField()
    sm3=models.IntegerField()

