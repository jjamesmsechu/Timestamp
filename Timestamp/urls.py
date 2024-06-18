from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home),
    path('history/',views.Saved),
    path('hours-manager/',views.Hours),
]