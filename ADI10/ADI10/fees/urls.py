
from django.urls import path
from .import views

urlpatterns = [ 
    path('one/',views.learn_django),
    path('two/',views.learn_python)
]