from django.db import models

# Create your models here.


class CartModel(models.Model):

	pro_id = models.IntegerField()
	pro_name = models.CharField(max_length=100)
	pro_brand = models.CharField(max_length=100)
	pro_quantity = models.CharField(max_length=100)
	pro_price = models.IntegerField()
	pro_size = models.IntegerField()

	class Meta:
		db_table = 'cart'