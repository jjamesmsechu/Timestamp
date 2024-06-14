from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home),
    path('saved-hours/',views.Hours),
    path('hours-manager/',views.Hours),
]