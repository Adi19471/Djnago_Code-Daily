from django.urls import path
from .import views

urlpatterns = [
    path('django/',views.learn_djcourse),
    path('python/',views.learn_djfees),
]
