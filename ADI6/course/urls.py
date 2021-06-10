from django.urls import path
from .import views

urlpatterns = [
   
    path('learn_html/',views.Html),
    path('learn_css/',views.css),

]