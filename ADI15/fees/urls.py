from django.urls import path
from . import views

urlpatterns  = [
    path('df/',views.dfees),
    path('pf/',views.pfees),
]