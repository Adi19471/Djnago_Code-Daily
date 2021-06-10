from django.urls import path
from Display import views

urlpatterns = [
    path('',views.display,name='disp'),
]