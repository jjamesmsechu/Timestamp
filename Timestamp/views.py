from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import hm_hours
from .models import Work_Day
import datetime

# Create your views here.
def Home(request):
    return render(request,'Timestamp/home.html',)

def Post(request):
    return render(request,'Timestamp/hours.html',)


def Hours(request):
    if request.method == "POST":

        workday = Work_Day.objects.create(time = request.POST['num_hours'], date = request.POST['date'])
    return render(request,'Timestamp/hours.html',{"workday":workday})