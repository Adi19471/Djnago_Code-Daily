from django.urls import path 
from course import views

urlpatterns = [
    path('dj/',views.django),
    path('py/',views.python),
]