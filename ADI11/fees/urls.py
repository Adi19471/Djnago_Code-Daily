from django.urls import path
from .import views


urlpatterns = [
    path('djs/',views.django_fees),
    path('pys/',views.python_fees),
]