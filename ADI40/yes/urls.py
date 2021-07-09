from django.urls import path
from yes import views

urlpatterns = [
    path('',views.home,name='django'),
]
