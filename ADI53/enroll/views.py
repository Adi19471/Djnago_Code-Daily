from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'enroll/home.html')
# def show (request,my_id):
#     student = {'id':my_id}
#     return render(request, 'enroll/show.html',student)


def show (request,my_id):
    if my_id ==1:
        student ={'id':my_id, 'name':'chinna'}
    if my_id ==1:
        student ={'id':my_id, 'name':'chinna'}
    if my_id ==1:
        student ={'id':my_id, 'name':'chinna'}
    return render(request, 'enroll/show.html',student)