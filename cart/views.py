from django.shortcuts import render,redirect
from django.http import HttpResponse
from cart.models import CartModel
from cart.forms import CartForm

# Create your views here.

def add_to_cart(request):

	if request.method == 'POST':

		form = CartForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('/cart/pro_deltails/')
			#return HttpResponse('data inserted')
		# else:
		# 	return HttpResponse('Error')
	else:
		form = CartForm()
	return render(request,'single.html',{'form':form})


def pro_deltails(request):

	data = CartModel.objects.all()
	price = CartModel.objects.values_list('pro_price', flat=True)
	quant = CartModel.objects.values_list('pro_quantity', flat=True)
	total = [a*b for a,b in zip(price,quant)]
	#return HttpResponse(total)

	return render(request,'vender.html',{'pro':data,'total':total})