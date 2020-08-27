from django.contrib import admin

# Register your models here.

# from slider.models import SliderModel
from .models import SliderModel

admin.site.register(SliderModel)