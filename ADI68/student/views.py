from django.shortcuts import render
from datetime import datetime
# Create your views here.
def setcookie(request):
    response = render(request, 'student/setcookie.html')
    response.set_cookie('name' ,'sonam')
    return response

def getcookie(request):
    name = request.COOKIES.get('name','ADI')
    now = datetime.utcnow()
    return render(request, 'student/getcookie.html',{'name':name,'ss':now})

# def sercookie(request):
#     return render(request, 'student/setcookie.html')