from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'Timestamp/home.html')
def Hours(request):
    return render(request,'Timestamp/hours.html')