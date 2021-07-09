from django.shortcuts import render,HttpResponseRedirect

from .forms import SignupForm,LoginForm,PostForm

from django.contrib import messages

from django.contrib.auth import authenticate,login,logout

from .models import Post


# home page
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html',{'posts':posts})

#about page
def about(request):
    return render(request, 'blog/about.html')

# contact page
def contact(request):
    return render(request, 'blog/contact.html')

# dahsboard page
def dashbord(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        messages.info(request,'you enter DashBoard....!!!','dont you want dashboed then click okay')
        return render(request, 'blog/dashbord.html',{'posts':posts})
    else:
        return HttpResponseRedirect('/login/')

# logout page
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

#signup page
def user_signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            messages.info(request,'Congratulation..!! You have become a Author')
            form.save()
    else:
     form = SignupForm()
    return render(request, 'blog/signup.html',{'form':form})

# login page
def user_login(request):
 if not request.user.is_authenticated:
  if request.method == "POST":
   form = LoginForm(request=request, data=request.POST)
   if form.is_valid():
    uname = form.cleaned_data['username']
    upass = form.cleaned_data['password']
    user = authenticate(username=uname, password=upass)
    if user is not None:
     login(request, user)
     messages.success(request, 'Logged in Successfully !!')
     return HttpResponseRedirect('/dashbord/')
  else:
   form = LoginForm()
  return render(request, 'blog/login.html', {'form':form})
 else:
  return HttpResponseRedirect('/dashbord/')


# add new post

def add_post(request):
    if request.user.is_authenticated:
        if request.method =='POST':
            form = PostForm(request.POST)
            if form.is_valid():
               ti = form.cleaned_data['title']
               de = form.cleaned_data['desc']
               dt = form.cleaned_data['date_time']
               user = Post(title=ti,desc=de,date_time=dt)
               user.save()
               messages.warning(request,'you go to dashboard MENU okay....?')
               form = PostForm()
        else:
            form = PostForm()
        return render(request,'blog/addpost.html',{'form':form})
    else:
        return HttpresponseRedirect('/login/')

# update post
def update_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST,instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi = Post.objects.get(pk=id)
            form = PostForm(instance=pi)

        return render(request,'blog/update.html',{'form':form})
    else:
        return HttpresponseRedirect('/login/')
 
# delete post
# def delete_post(request,id):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#           pi = Post.objects.get(pk = id)
#           pi.delete()
#           return HttpresponseRedirect('/dashbord/'
#     else:
#       return HttpresponseRedirect('/login/')

def delete_post(request, id):
  if request.user.is_authenticated:
    if request.method == 'POST':
      pi = Post.objects.get(pk = id)
      pi.delete()
      return HttpResponseRedirect('/dashbord/')
  else:
    return HttpResponseRedirect('/login/')
 