from django.db import models

from django.core.validators import RegexValidator
class DemoModel(models.Model):

	name_regex = RegexValidator(r'^[a-zA-Z ]*$', 'Only alphabets allowed.')
	deg_regex = RegexValidator(r'^[a-zA-Z ]*$', 'Only alphabets allowed.')
	name = models.CharField(max_length=50,validators=[name_regex])
	email = models.EmailField()
	mobile = models.BigIntegerField()
	salary = models.IntegerField()
	designation = models.TextField(max_length=50,default="",validators=[deg_regex])
	address = models.TextField()

	class Meta:

		db_table = 'demo'
	# def __str__(self):
	# 	return self.name
		
	# def __int__(self):
	# 	return self.salary
