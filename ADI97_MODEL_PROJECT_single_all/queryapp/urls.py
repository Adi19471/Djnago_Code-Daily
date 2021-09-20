from django.urls import path
from queryapp import views 

urlpatterns = [
    path('<int:id>/',views.home_view)
]