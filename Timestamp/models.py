from django.db import models
import time
import datetime
# Create your models here.
class Work_Day(models.Model):
    date = models.DateField(default=datetime.date.today)
    startime = models.TimeField(default= datetime.time(hour=1,minute=4))
    endtime = models.TimeField(default=datetime.time(1,2,3))
    seconds = models.FloatField(default=0)
    difference = models.TextField(default= "")
def __str__(self):
    return self.date

