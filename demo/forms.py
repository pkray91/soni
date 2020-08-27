from django import forms

from demo.models import DemoModel

class DemoForm(forms.ModelForm):
	class Meta:
		model = DemoModel
		# fields = ['name','mobile','salary']
		fields = "__all__"	