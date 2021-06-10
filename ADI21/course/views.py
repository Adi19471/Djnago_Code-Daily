from django.shortcuts import render

# Create your views here.
def course_data(request):
    return render(request, 'course/course_data.html'),