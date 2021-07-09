from django.shortcuts import render

# Create your views here.
def home(request):
    ct = request.session.get('count',0)
    new = ct + 1
    request.session['count'] = new

    return render(request, 'os/home.html',{'my':new})