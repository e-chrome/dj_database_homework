import csv
from datetime import datetime
from django.utils.text import slugify
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
        date_formatter = "%Y-%m-%d"
        for phone in phones:
            id = phone['id']
            name = phone['name']
            image = phone['image']
            price = int(phone['price'])
            release_date = datetime.strptime(phone['release_date'], date_formatter).date()
            lte_exists = bool(phone['lte_exists'])
            slug = slugify(phone['name'])
            Phone.objects.create(
                id=id,
                name=name,
                image=image,
                price=price,
                release_date=release_date,
                lte_exists=lte_exists,
                slug=slug
            )
