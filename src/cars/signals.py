from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User
from .models import Car
from django.dispatch import receiver
import uuid as u
from buyers.models import Buyer


# @receiver(pre_save, sender=Car)
# def pre_save_create_code(sender, instance, **kwargs):
# 	if instance.code == '':
# 		instance.code == str(u.uuid4()).replace('-', '').upper()[:5]
# 	print(Buyer.objects.get(user=instance.buyer.user))
# 	obj = Buyer.objects.get(user=instance.buyer.user)
# 	obj.from_signal = True
# 	obj.save()

@receiver(post_save, sender=Car)
def post_save_code_change_user(sender, instance, **kwargs):
	if instance.code == '':
		instance.code == str(u.uuid4()).replace('-', '').upper()[:5]
		instance.save()

	obj 			= Buyer.objects.get(user=instance.buyer.user)
	obj.from_signal = True
	obj.save()