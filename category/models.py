from django.db import models


class CategoryModel(models.Model):

	cat_name = models.CharField(max_length=100)

	class Meta:

		db_table = 'categoty'
		verbose_name = 'categoty List'

	def __str__(self):
		return self.cat_name