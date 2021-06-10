from django.shortcuts import render

# Create your views here.
def  python_fees(request):
    return render(request, 'fees/feesone.html')

def  django_fees(request):
    return render(request, 'fees/feestwo.html')