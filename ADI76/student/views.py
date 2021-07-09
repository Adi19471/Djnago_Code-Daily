from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime



def setsession(request):
    request.session['name'] = 'Adi'
    return render(request, 'student/setsession.html')




def getsession(request):
     now = datetime.now()
     name = request.session['name']
     return render(request, 'student/getsession.html',{'name':name,'now':now})
 
def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'student/delsession.html')