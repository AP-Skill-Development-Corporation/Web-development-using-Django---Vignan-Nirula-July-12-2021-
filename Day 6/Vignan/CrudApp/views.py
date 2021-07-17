from django.shortcuts import render,redirect
from django.http import HttpResponse
from CrudApp.models import Student
# Create your views here.
def demo(request):
	return HttpResponse('From CrudApp')

def register(request):
	if request.method == 'POST':
		na = request.POST.get('name')
		rno = request.POST.get('rnum')
		age = request.POST.get('age')
		mob = request.POST.get('mob')
		em = request.POST.get('email')
		addr = request.POST.get('addr')
		Student.objects.create(name=na,rollnum=rno,age=age,
							mobile=mob,email=em,address=addr)
		return redirect('/crud/details')
	return render(request,'CrudApp/register.html')

def details(request):
	data = Student.objects.all()
	return render(request,'CrudApp/details.html',{'data':data})


def update(request,id):
	info = Student.objects.get(id=id)
	if request.method == 'POST':
		info.name = request.POST['name']
		info.rollnum = request.POST['rnum']
		info.age = request.POST['age']
		info.mobile = request.POST['mob']
		info.email = request.POST['email']
		info.address = request.POST['addr']
		info.save()
		return redirect('/crud/details/')
	return render(request,'CrudApp/update.html',{'info':info})


def delete(request,id):
	userinfo = Student.objects.get(id=id)
	if request.method == 'POST':
		userinfo.delete()
		return redirect('/crud/details/')
	return render(request,'CrudApp/delete.html',{'userinfo':userinfo})












