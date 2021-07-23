from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


def home(request):
	return render(request,"home.html")

def register(request):
	if request.method=='POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("Registration Successful!")
		else:
			return HttpResponse("Invalid Data")
	form = RegistrationForm()
	return render(request,"register.html",{'form':form})


def signin(request):
	if request.method=="POST":
		username = request.POST['uname']
		password = request.POST['pswd']
		user = authenticate(username=username,password = password)
		if user:
			login(request,user)
			return redirect('home')
		else:
			return HttpResponse("Invalid Credentials")
	return render(request,"login.html")


def signout(request):
	messages.info(request,"logged out of the session")
	logout(request)
	return redirect("login")