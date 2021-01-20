from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Buyer

# post save signals -> executa depois de um modelo ser salvo
@receiver(post_save, sender=User) 
		#SENDER -> nesse caso, sempre que uma instância de usuário
		#for criada, mandaremos um sinal para que uma instância de buyer seja criada também
def post_save_create_buyer(sender, instance, created, **kwargs):
	print('sender: ', sender)
	print('instance: ', instance)
	print('created: ', created)
	if created: #if the instance is created
		Buyer.objects.create(user=instance)