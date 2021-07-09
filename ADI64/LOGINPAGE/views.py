from django.shortcuts import render,HttpResponseRedirect
from .forms import UserCreationForm
# authentication form import from form
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
# messages 
from django .contrib import messages
# login logout authenticate
from django.contrib.auth import authenticate,login,logout
# Create your views here.


def sign_up(request):
    if request.method =="POST":
     fm = UserCreationForm(request.POST)
     if fm.is_valid():
         fm.save()
    else:
        fm = UserCreationForm()
    return render(request, 'LOGINPAGE\sign_up.html',{'form':fm})


#login_view

def user_login(request):
    if request.method =="POST":
     fm = AuthenticationForm(request=request,data=request.POST)
     if fm.is_valid():
        uname = fm.cleaned_data['username']
        upass = fm.cleaned_data['password']
        user = authenticate(username=uname,password=upass)
        if user is not None:
          login(request,user)
          return HttpResponseRedirect("/profile/")
    else:
       fm = AuthenticationForm()
    return render(request,'LOGINPAGE/userlogin.html',{'form':fm})

# profile Login_page

# def user_login(request):
#   if not request.user.is_authenticated:
#     if request.method == "POST":
#       fm = AuthenticationForm(request=request, data=request.POST)
#       if fm.is_valid():
#         uname = fm.cleaned_data['username']
#         upass = fm.cleaned_data['password']
#         user = authenticate(username=uname, password=upass)
#         if user is not None:
#           login(request, user)
#           messages.success(request, 'Logged in successfully !!')
#           return HttpResponseRedirect('/profile/')
#     else: 
#       fm = AuthenticationForm()
#     return render(request, 'LOGINPAGE/userlogin.html', {'form':fm})

def user_profile(request):
    return render(request,'LOGINPAGE/profile.html',{'name':request.user})


#logout

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

# chainge passwprd to old password 
def chainge_pass(request):
    if request.method == 'POST':
        fm = PasswordChangeForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/profile/')
    else:

        fm = PasswordChangeForm(request.POST)
    return render(request, 'LOGINPAGE/chainge.html',{'form':fm})
    

