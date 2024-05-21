from django.core.management.base import BaseCommand
from products.models import Product
from faker import Faker
import random


class Command(BaseCommand):
    help = 'Crea 30 nuevos productos con un nombre y un precio'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(30):
            name = fake.unique.word().capitalize()
            price = round(random.uniform(10.0, 100.0), 2)
            Product.objects.create(name=name, price=price)

        self.stdout.write(self.style.SUCCESS('Se han creado 30 nuevos productos con éxito.'))
