from django .urls import path
# app import from app to views
from django.conf.urls.static import static
from django.conf import  settings

from Gallery import views

urlpatterns =[
    path('',views.gallery_page,name="gallery"),
    
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)