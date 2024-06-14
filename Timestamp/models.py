from django.db import models
import time
import datetime
# Create your models here.
class Work_Day(models.Model):
    time = models.IntegerField()
    date = models.DateField( default= datetime.datetime.today())

def __str__(self):
    return self.time
