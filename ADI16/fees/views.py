from django.shortcuts import render
# from django.http import HttpResponse


# Create your views here.
def django_fees(request):
    return render(request,'pay/fone.html')


def python_fees(request):
    return render(request,'pay/feestwo.html')