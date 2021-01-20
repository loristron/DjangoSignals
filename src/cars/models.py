from django.db import models
from buyers.models import Buyer
import uuid as u 

# Create your models here.
class Car(models.Model):
	name		= models.CharField(max_length=200)
	price		= models.PositiveIntegerField()
	buyer		= models.ForeignKey(Buyer, on_delete=models.CASCADE )
	code 		= models.CharField(max_length=10, blank=True)

	def __str__(self):
		return f'{self.name}-{self.price}-{self.buyer}'

	# def save(self, *args, **kwargs):
	# 	if self.code == '':
	# 		self.code = str(u.uuid4()).replace('-', '').upper()[:5]
	# 	return super().save(*args, **kwargs)
