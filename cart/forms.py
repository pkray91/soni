from django import forms

from cart.models import CartModel

class CartForm(forms.ModelForm):
	class Meta:
		model = CartModel
		# fields = ['name','mobile','salary']
		fields = "__all__"	