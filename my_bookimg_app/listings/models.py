from django.db import models
class listing(models.Model)
host_id=models.AutoFieldField(primary_key=True)
title =models.CharField(max_length=10)
descriptino =models.TextFieldField(blank=True, null=True)
location =models.CharField(max_length=10)
latitude =models.DecimalField(max_digits=7, decimal_places=5)
price_per_night =models.DecimalField(max_digits=7, decimal_places=5)
cleaning_fee = models.DecimalField(max_digits=7, decimal_places=5)
max_guests = models.IntegerField()
is_active =models.BooleanField(default=True)
created_at =models.DateTimeField(auto_now_add=True)
updated_at =models.DateTimeField(auto_now_add=True)
def __str__(self):
    return self.name


class listing_image(models.Model)
image_url =models.URLField()
is_primary =models.BooleanField(default=False)
def __str__(self):
    return self.name

class listing_amenity(models.Model)
listing_id = models.AutoField(primary_key=True)
amenities_id = models.AutoField(primary_key=True)
def __str__(self):
    return self.name

class availability(models.Model)
listing_id = models.AutoField(primary_key=True)
date =models.DateField()
is_available =models.BooleanField(default=True)
def __str__(self):
    return self.name