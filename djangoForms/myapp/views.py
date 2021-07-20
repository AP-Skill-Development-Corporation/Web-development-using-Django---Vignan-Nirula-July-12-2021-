from django.shortcuts import render,redirect
from .forms import LibraryForm
from django.http import HttpResponse
from .models import library
from django.core.mail import send_mail
from djangoForms import settings
# Create your views here.


def add_book(request):
	if request.method=='POST':
		form = LibraryForm(request.POST)
		if form.is_valid():
			form.save()
			# return HttpResponse("succesful")
			return redirect('books')
		else:
			return HttpResponse("Invalid Data")
	form = LibraryForm()
	return render(request,"add_book.html",{"form":form})


def books(request):
	data = library.objects.all()
	return render(request,"books.html",{"data":data})

def update(request,book_no):
	data = library.objects.get(book_no = book_no)
	form = LibraryForm(instance=data)
	if request.method=="POST":
		form = LibraryForm(request.POST,instance=data)
		if form.is_valid():
			form.save()
			return redirect('books')
		else:
			return HttpResponse("Invalid data")
	return render(request,"update.html",{"form":form})

def delete(request,book_no):
	data = library.objects.get(book_no = book_no)
	data.delete()
	return redirect("books")



def contact_us(request):
	if request.method=='POST':
		sender = request.POST['mail']
		body = request.POST['query']
		sub = "Query"
		receiver = settings.EMAIL_HOST_USER
		send_mail(sub,body,sender,[receiver])
		return HttpResponse("Mail sent!")

	return render(request,"contact_us.html")


