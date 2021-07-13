from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
	return HttpResponse('Welcome Page.......')

def demo(n):
	return HttpResponse('<h2 style = "background-color:skyblue;color:white;padding:3px;margin-left:230px;margin-right:230px">For demo purpose.....)</h2>')

def mesg(request,name):
	return HttpResponse('<h2>Hii... {} Welcome</h2>'.format(name))

def data(request,name,num):
	return HttpResponse('<h2>Hii ... {} Welcome your number is {} </h2>'.format(name,num))