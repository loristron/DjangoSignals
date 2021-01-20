from django.apps import AppConfig


class BuyersConfig(AppConfig):
    name = 'buyers'

    def ready(self):
    	import buyers.signals