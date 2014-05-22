from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.
class Car(models.Model):
	company = models.CharField(max_length = 120, null = True, blank = True)
 	model = models.CharField(max_length = 120, null = True, blank = True)
 	email = models.EmailField()
 	

 	def __unicode__(self):
 		return smart_unicode(self.email)