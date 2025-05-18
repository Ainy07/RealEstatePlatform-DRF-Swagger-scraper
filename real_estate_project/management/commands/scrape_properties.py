
from django.core.management.base import BaseCommand
from real_estate.scraper import scrape_properties

class Command(BaseCommand):
    help = 'Scrapes real estate property data'

    def handle(self, *args, **kwargs):
        scrape_properties()
        self.stdout.write(self.style.SUCCESS("Scraping finished!"))
