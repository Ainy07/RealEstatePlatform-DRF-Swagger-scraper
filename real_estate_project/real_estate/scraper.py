from builtins import float
import requests
from bs4 import BeautifulSoup
from .models import Property

def scrape_properties():
    print("Dummy scraper is running...")
    url = "https://example.com/properties" 
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    listings = soup.find_all("div", class_="property-card") 

    for listing in listings:
        title = listing.find("h2").text.strip()
        location = listing.find("span", class_="location").text.strip()
        price = float(listing.find("span", class_="price").text.replace("$", "").replace(",", ""))
        area = float(listing.find("span", class_="area").text.replace("sqft", "").strip())

        Property.objects.get_or_create(
            title=title,
            location=location,
            price=price,
            area_sqft=area
        )
