from django.shortcuts import render
from .forms import ImagesForm
# Create your views here.
from django.http import HttpResponse
from .models import Images


def files(request):
	if request.method=='POST':
		form = ImagesForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponse("File uploaded Successfully!")
		else:
			return HttpResponse("Invalid Data")
	form = ImagesForm()
	return render(request,"files.html",{'f':form})



def gallery(request):
	data = Images.objects.all()
	return render(request,"gallery.html",{'data':data})

