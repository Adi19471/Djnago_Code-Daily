from django.shortcuts import render
from .forms import ImagesForm
from .models import Image

# Create your views here.
def gallery_page(request):
    if request.method == 'POST':
        form = ImagesForm(request.POST,request.FILES)
        if form.is_valid():
         form.save()
            # # na =form.cleaned_data['name']
            # im = form.cleaned_data['image']
            # da = form.cleaned_data['date']
            # user = Image(image=im,date=da)
            # user.save()
            # form = ImagesForm()
    else:
         form = ImagesForm()
    tops = Image.objects.all()
    return render(request,'Gallery/gallery_page.html',{'form':form,'top':tops})