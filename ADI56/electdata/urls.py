from django.urls import path
from electdata import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.student,name='student')
]
