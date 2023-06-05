import csv
from datetime import datetime

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    help = "Import phones from csv file"

    def handle(self, *args, **options):
        with open("phones.csv", "r") as csvfile:
            phone_reader = csv.reader(csvfile, delimiter=";")
            next(phone_reader)

            for row in phone_reader:
                print(row)
                id, name, image, price, release_date_str, lte_exists_str = row
                release_date = datetime.strptime(release_date_str, "%Y-%m-%d").date()
                lte_exists = lte_exists_str.lower() == "true"
                phone = Phone(
                    id=id,
                    name=name,
                    image=image,
                    price=price,
                    release_date=release_date,
                    lte_exists=lte_exists,
                )
                phone.save()
        self.stdout.write(self.style.SUCCESS("Phones have been imported successfully!"))
