from django.urls import path
from course import views

urlpatterns = [
    path('dj/',views.django_course),
    path('py/',views.python_course),
]