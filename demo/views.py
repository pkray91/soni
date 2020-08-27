from django.shortcuts import render,redirect
from django.http import HttpResponse
from demo.models import DemoModel
from demo.forms import DemoForm
from django.db.models import Sum,Avg, Max, Min,Count

# Create your views here.
def home(requset):
	return render(requset,'home.html')
def about(requset):
	return render(requset,'about.html')
def services(requset):
	return render(requset,'services.html')
def contact(requset):
	return render(requset,'contact.html')
def form(requset):
	return render(requset,'form.html')
def formdata(requset):
	
	# if requset.method == 'GET':
	# 	name = requset.GET.get('name')
	# 	email = requset.GET.get('email')
	# 	mobile = requset.GET.get('mobile')
	# 	salary = requset.GET.get('salary')
	# 	address = requset.GET.get('address')
	# 	data = [name,email,mobile,salary,address]

	# name = requset.POST.get('name')
	# email = requset.POST.get('email')
	# mobile = requset.POST.get('mobile')
	# salary = requset.POST.get('salary')
	# address = requset.POST.get('address')
	# data = [name,email,mobile,salary,address]

	# return HttpResponse(data)
	if requset.method == 'POST':

		form = DemoForm(requset.POST)

		if form.is_valid():
			form.save()
			return redirect('/getdata/')
			#return HttpResponse('data inserted')
		# else:
		# 	return HttpResponse('Error')
	else:
		form = DemoForm()
	return render(requset,'form.html',{'form':form})

def getdata(requset):

	data = DemoModel.objects.all()
	# total_sal = DemoModel.objects.all().aggregate(Sum('salary'))
	# min_sal = DemoModel.objects.all().aggregate(Min('salary'))
	# max_sal = DemoModel.objects.all().aggregate(Max('salary'))
	# avg_sal = DemoModel.objects.all().aggregate(Avg('salary'))
	# no_of_record = DemoModel.objects.all().aggregate(Count('salary'))
	# sal = DemoModel.objects.all().order_by('salary')
	# return HttpResponse(sal)
	# quit()
	# data = DemoModel.objects.all()[:3] //limit
	# data = DemoModel.objects.all().order_by('salary')[:3]
	# data = DemoModel.objects.all().order_by('-salary')[:3]
	# data = DemoModel.objects.all().order_by('-salary')[2:5]#[2(kitna chodna ):3(kitne total lena hai)]3-2 =1
	# data = DemoModel.objects.all().order_by('salary')
	# data = DemoModel.objects.all().order_by('salary').reverse()
	# data = DemoModel.objects.all().order_by('salary')[::-1]
	# data = DemoModel.objects.all().order_by('-salary')
	# data = DemoModel.objects.filter(salary = 7000)
	# data = DemoModel.objects.exclude(salary = 7000)
	# return render(requset,'showdata.html',{'content':data})
	# return render(requset,'tabledata.html',{'content':data,'tsal':total_sal,'min':min_sal,'max':max_sal,'avg':avg_sal,'count':no_of_record})
	return render(requset,'tabledata.html',{'content':data})
def delete(requset,id):

	# return HttpResponse(id)
	data = DemoModel.objects.get(id=id)

	if data.delete():
		return redirect('/getdata/')

def getdataforedit(requset,id):

	# return HttpResponse(id)
	data = DemoModel.objects.get(id=id)
	return render(requset,'editdata.html',{'content':data});

def editdata(request,id):
	if request.method == "GET":
		emp = DemoModel.objects.get(id=id)
		form = DemoForm(request.GET,instance=emp)
		if form.is_valid():
			try:
				form.save()
				return redirect('/getdata')
			except:
				pass
	else:
		form = DemoForm()
	return render(request,"editdata.html",{'form':form})


def test1(requset):

	return HttpResponse('Hello django')

def test2(requset):
	return HttpResponse('<h1 style="color:green;text-align:center"> My name <br> is Harshit </h1>')

def test3(requset):

	a = 20
	b = 7
	c= a+b 
	d= a-b 
	e= a*b 
	f= a/b 
	g= a%b 
	cal = [c,' ',d,' ',e,' ',f,' ',g]
	return HttpResponse(cal)

def test4(requset):

	num = 25;

	if num%2==0:
		return HttpResponse('even no')

	else:
		return HttpResponse('odd no')

def test5(requset):

	return render(requset,'test.html')

def test6(requset):

	if requset.method == "GET":

		num = int(requset.GET["num"])

		if num%2==0:
			return HttpResponse('even no')

		else:
			return HttpResponse('odd no')

def test7(requset):

	return render(requset,'cal.html')

def cal(requset):

	if requset.method == "GET":

		num1 = requset.GET['num1']
		num2 = requset.GET['num2']
		a = int(num1)
		b = int(num2)
		add = requset.GET.get('add')
		sub = requset.GET.get('sub')
		mul = requset.GET.get('mul')
		div = requset.GET.get('div')
		rem = requset.GET.get('rem')

		if add:	
			v1 = a+b
			return render(requset,'cal.html',{'data':v1})
			#return HttpResponse(a+b)
		elif sub:
			v2 = a-b
			return render(requset,'cal.html',{'data':v2})
			#return HttpResponse(a-b)
		elif mul:
			v3 = a*b
			return render(requset,'cal.html',{'data':v3})
			#return HttpResponse(a*b)
		elif div:
			v4 = a/b
			return render(requset,'cal.html',{'data':v4})
			#return HttpResponse(a/b)
		elif rem:
			v5 = a%b
			return render(requset,'cal.html',{'data':v5})
			#return HttpResponse(a%b)



