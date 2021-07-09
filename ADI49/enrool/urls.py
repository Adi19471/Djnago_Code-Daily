from django.urls import path
from enrool import views

urlpatterns = [
    path('',views.home_view)
]
