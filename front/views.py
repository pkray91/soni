from django.shortcuts import render
from django.http import HttpResponse
from product.models import ProductModel
from category.models import CategoryModel
from slider.models import SliderModel
def index(requset):

	product  = ProductModel.objects.all()
	slider = SliderModel.objects.all()
	cat = CategoryModel.objects.all()
	return render(requset,'index.html',{'mycat':cat,'sal':slider,'pro':product})

def register(requset):

	return render(requset,'registered.html')
def login(requset):

	return render(requset,'login.html')


def contact(requset):

	return render(requset,'contact.html')

def products(requset):

	return render(requset,'products.html')
def single(requset,id):
	#return HttpResponse(id)
	data = ProductModel.objects.get(id=id)
	return render(requset,'single.html',{'value':data})

