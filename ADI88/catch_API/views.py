from django.shortcuts import render

from django.core.cache import  cache

# # Create your views here.
# def home_view(request):
#     mv = cache.get('movie','has_expired')
#     if mv == 'has_expired':
#         cache.set('movie','The One', 30)
#         mv = cache.get('movie')
#     return render(request, 'catche/s.html',{'fm':mv})


# def home_view(request):
#     mv = cache.get_or_set('fees' , 500, 10 , version = 2)
    
#     return render(request, 'catche/s.html',{'fm':mv})


# def home_view(request):
#     dv = cache.delete('fees',version = 2)
#     print(dv)
    
#     return render(request, 'catche/s.html') 

# def home_view(request):
#     dv = cache.incr('roll',delta = 2)
#     print(dv)
    
#     return render(request, 'catche/s.html') 

def home_view(request):
    dv = cache.clear()
    print(dv)
    
    return render(request, 'catche/s.html') 