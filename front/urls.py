from django.urls import path

from front import views
from sonu import settings
from django.conf.urls.static import static


urlpatterns = [
	
	path('',views.index,name='index'),
	path('register/',views.register,name='register'),
	path('login/',views.login,name='login'),
	path('contact/',views.contact,name='contact'),
	path('products/',views.products,name='products'),
	path('single/<int:id>/',views.single,name='single'),

]

if settings.DEBUG:
    #urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)