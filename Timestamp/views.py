from django.shortcuts import render
from django import forms

# Create your views here.
def Home(request):
    return render(request,'Timestamp/home.html')
def Hours(request):
    return render(request,'Timestamp/hours.html')