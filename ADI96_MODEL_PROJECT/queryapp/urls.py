from django.urls import path
from queryapp import views 

urlpatterns = [
    path('',views.home_view)
]