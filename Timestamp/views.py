from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Work_Day
from datetime import timedelta, datetime , date 
import time 
from time import strptime

# Create your views here.
def Home(request):
    return render(request,'Timestamp/home.html',)

def Post(request):
    return render(request,'Timestamp/hours.html',)

def Saved(request):
    return render(request,'Timestamp/saved.html')




def Hours(request):
    if request.method == "POST":
        startime = request.POST['startime']
        endtime = request.POST['endtime'] 
        time_diff = strptime(startime,"%H:%M")
        time_diff2 = strptime(endtime,'%H:%M')
        time_diff = timedelta(hours=time_diff2.tm_hour,minutes=time_diff2.tm_min) - timedelta(hours=time_diff.tm_hour, minutes=time_diff.tm_min)
        second = time_diff.total_seconds()
        workday = Work_Day.objects.create(seconds = second, startime = request.POST['startime'], endtime = request.POST['endtime'] , date = request.POST['date'], difference = str(time_diff))

        
    return render(request,'Timestamp/hours.html',{"workday":workday,"time_diff": time_diff})