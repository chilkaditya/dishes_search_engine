import csv
from django.core.management.base import BaseCommand
from restaurant.models import Restaurant

class Command(BaseCommand):
    help = 'Load restaurants from a CSV file'

    def handle(self, *args, **kwargs):
        with open('restaurants_small.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Restaurant.objects.create(
                    name=row['name'],
                    location=row['location'],
                    items=row['items'],
                    # lat_long = row['lat_long'],
                    full_details=row['full_details']
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from CSV'))
