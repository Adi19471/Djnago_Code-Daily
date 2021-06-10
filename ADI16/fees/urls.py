from django.urls import path
from fees import views

urlpatterns = [
    path('fd/',views.django_fees),
    path('fp/',views.python_fees),
]
