from django.shortcuts import render

# Create your views here.
def shops(request):
    return render(request,'enroll/shops.html')