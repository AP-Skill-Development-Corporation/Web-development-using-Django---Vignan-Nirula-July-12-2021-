from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def demo(request):
	return HttpResponse('From Basic App.........')

def bdemo(request):
	return render(request,'BasicApp/bdemo.html')

def register(request):
	return render(request,'BasicApp/register.html')


def login(request):
	return render(request,'BasicApp/login.html')

