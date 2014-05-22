from django.contrib import admin

# Register your models here.
from models import Car

class CarAdmin(admin.ModelAdmin):
	class Meta:
		model = Car

admin.site.register(Car, CarAdmin )