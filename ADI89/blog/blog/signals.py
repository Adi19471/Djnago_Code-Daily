from django.contrib.auth.signals import user_logged_in, user_logged_out,user_login_failed

from django.contrib.auth.models import  User 

def login_success(sender,request,user,**kwargs):
  print("____________++++++++++++++++++++++++++++++")
  print("Logout in Signals ........................Run intro")
  print("sender:",sender)
  print("USer:" ,user)
  print(f"kwargs:",{kwargs})
  
  user_logged_in.conncet(login_success,sender=User)
  
  