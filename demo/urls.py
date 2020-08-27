from django.urls import path

from demo import views

urlpatterns = [

		path('demo1/',views.test1,name='test1'),
		path('demo2/',views.test2,name='test2'),
		path('demo3/',views.test3,name='test3'),
		path('demo4/',views.test4,name='test4'),
		path('demo5/',views.test5,name='test5'),
		path('demo6/',views.test6,name='test6'),
		path('demo7/',views.test7,name='test7'),
		path('cal/',views.cal,name='cal'),
		path('home/',views.home,name='home'),
		path('about/',views.about,name='about'),
		path('services/',views.services,name='services'),
		path('contact/',views.contact,name='contact'),
		path('form/',views.form,name='form'),
		path('formdata/',views.formdata,name='formdata'),
		path('getdata/',views.getdata,name='getdata'),
		path('delete/<int:id>',views.delete,name='delete'),
		path('getdataforedit/<int:id>',views.getdataforedit,name='getdataforedit'),
		path('editdata/<int:id>',views.editdata,name='editdata'),
		

]