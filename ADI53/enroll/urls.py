from django .urls import path

from enroll import views


urlpatterns = [
    path('home/',views.home,name='home'),
    path('show/<int:my_id>/',views.show,name='detail'),
]
