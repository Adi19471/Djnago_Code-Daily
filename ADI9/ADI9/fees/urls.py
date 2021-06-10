from django.urls import path
from django.urls.resolvers import URLPattern
from .import views

URLPatterns = [ 
    path('feesdj/',views.django_fees),
    path('feespy/',views.python_fees),

]