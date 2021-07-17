from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def demo(request):
	return HttpResponse('From Basic App.........')

def bdemo(request):
	return render(request,'BasicApp/bdemo.html')

def register(request):
	if request.method == 'POST':
		un = request.POST['uname']
		em = request.POST['email']
		ps = request.POST['pswd']
		cps = request.POST['cpswd']
		gn = request.POST['optradio']
		dob = request.POST['dob']
		ln = request.POST.getlist('lan')
		c = request.POST['course']
		r = request.POST['range']
		f = request.POST['file']
		cm = request.POST['txt']
		#print(un,em,ps,cps,gn,dob,ln,c,r,f,cm)
		return render(request,'BasicApp/details.html',{'username':un,'email':em,
					'gender':gn,'Dob':dob,'Lan':ln,'Course':c,'Range':r,'File':f,'Comment':cm})
	return render(request,'BasicApp/register.html')


def login(request):
	if request.method == 'POST':
		u = request.POST['uname']
		p = request.POST['pswd']
		if u == 'Apssdc' and p == 'Apssdc@123':
			return HttpResponse('<h2>Hii... Welcome {} </h2>'.format(u))
		else:
			return HttpResponse('<h2>Invalid username / password</h2>')
	return render(request,'BasicApp/login.html')

