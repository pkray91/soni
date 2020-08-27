from django.db import models

class ProductModel(models.Model):

	cat_name = models.CharField(max_length=50,default="")
	name = models.CharField(max_length=100)
	brand = models.CharField(max_length=100)
	color = models.CharField(max_length=50)
	image = models.FileField()
	size = models.CharField(max_length=100)
	price = models.IntegerField()
	category = models.CharField(max_length=100)
	details = models.TextField()

	class Meta:
		db_table = 'products'

	def __str__(self):
		return self.name