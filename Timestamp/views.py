from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import hm_hours

# Create your views here.
def Home(request):
    return render(request,'Timestamp/home.html')

def Post(request):
    return render(request,)


def Hours(request):
    if request.method == "POST":
        form = hm_hours(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("")
    else:
        form = hm_hours()

    return render(request,'Timestamp/hours.html',{"form":form})