from django.shortcuts import render

# Create your views here.
def dfees(request):
    return render(request,'fees/feesone.html')

def pfees(request):
    return render(request,'fees/feestwo.html')