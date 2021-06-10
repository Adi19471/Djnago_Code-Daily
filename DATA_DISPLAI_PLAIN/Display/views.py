from django.shortcuts import render

from.forms import AdharCard

# Create your views here.
def display(request):
    if request.method =="POST":
        fm = AdharCard(request.POST)
        print(fm)
        if fm.is_valid():
            print("okay")
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            messages = fm.cleaned_data['messages']
            password = fm.cleaned_data['password']

            print('PASWORD',password)
            print('Name',name)
            print('Email',email)
            print('Message',messages)
            print('CLEANED_DATA',fm.cleaned_data['password'])
            print('CLEANED_DATA',fm.cleaned_data['name'])
            print('CLEANED_DATA',fm.cleaned_data['email'])
            print('CLEANED_DATA',fm.cleaned_data['messages'])
            fm = AdharCard()
           

    else:
     fm = AdharCard()
     print("no option this data")
    return render (request,'Display/show.html',{'fm':fm})