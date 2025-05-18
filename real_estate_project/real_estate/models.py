from django.db import models

class Property(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    price = models.FloatField()
    area_sqft = models.FloatField()
    description = models.TextField(blank=True)
    listed_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='property_images/', blank=True, null=True)

    def __str__(self):
        return self.title
