
from django.contrib import admin
from django.urls import path,include
from front import views
from cart import views
from account import views

urlpatterns = [
	path('',include('front.urls')),
	path('cart/',include('cart.urls')),
	path('account/',include('account.urls')),
	#path('',include('demo.urls')),
    path('admin/', admin.site.urls),
]
