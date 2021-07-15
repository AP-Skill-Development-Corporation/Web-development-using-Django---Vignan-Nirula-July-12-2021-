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


def table(request,n):
	k = ""
	for i in range(1,11):
		k += "{}  X {:02} = {:02}".format(n,i,n*i) + "<br>"
	#print(k)
	return HttpResponse(k)

def dhtml(request):
	return render(request,'SampleApp/demo.html')


def details(request,name,n):
	return render(request,'SampleApp/details.html',{'na':name,'num':n})

def scss(request):
	return render(request,'SampleApp/samplecss.html')

def login(request):
	return render(request,'SampleApp/login.html')