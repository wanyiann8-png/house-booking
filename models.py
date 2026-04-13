from django.db import models
class user(models.Model):
user_name =models.CharField(max_length=100)
email =models.EmailField(unique=True)
password =models.CharField(max_length=100)
is_active =models.BooleanField(default=True)
created_at =models.DateTimeField(auto_now_add=True)
def __str__(self):
    return self.name


class amenities
name =models.CharField(max_length=100)
def __str__(self):
    return self.name


class profile(models.Model):
user_id =models.AutoField(primary_key=True)
full_name =models.CharField(max_length=100)
phone =models.CharField(max_length=10)
is_host =models.BooleanField(default=False)
avatar_url =models.URLField(blank=True, null=True)
bio =models.TextField(blank=True, null=True)
def __str__(self):
    return self.name


class listings(models.Model)
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


class wishlist(models.Model)
user_id = models.AutoField(primary_key=True)
name =models.CharField(max_length=100)
created_at =models.DateTimeField(auto_now_add=True)
def __str__(self):
    return self.name


class booking(models.Model)
user_id = models.AutoField(primary_key=True)
listing_id = models.AutoField(primary_key=True)
check_in =models.DateTimeField(auto_now_add=True)
check_out =models.DateTimeField(auto_now_add=True)
guests =models.IntegerField()
total_price =models.DecimalField(max_digits=7, decimal_places=5)
status =models.CharField(max_length=10)
created_at =models.DateTimeField(auto_now_add=True)
def __str__(self):
    return self.name


class listing_image(models.Model)
image_url =models.URLField()
is_primary =models.BooleanField(default=False)
def __str__(self):
    return self.name
class availability(models.Model)
listing_id = models.AutoField(primary_key=True)
date =models.DateField()
is_available =models.BooleanField(default=True)
def __str__(self):
    return self.name


class listing_amenities(models.Model)
listing_id = models.AutoField(primary_key=True)
amenities_id = models.AutoField(primary_key=True)
def __str__(self):
    return self.name
 
 
class wishlist_items(models.Model)
wishlist_id = models.AutoField(primary_key=True)
listing_id = models.AutoField(primary_key=True)
def __str__(self):
    return self.name


class payments(models.Model)
payment_id = models.AutoField(primary_key=True)
amount =models.DecimalField(max_digits=7, decimal_places=5)
payment_method =models.CharField(max_length=100)
status =models.CharField(max_length=10)
transaction_ref =models.CharField(max_length=100)
created_at =models.DateTimeField(auto_now_add=True)
def __str__(self):
    return self.name
 

class review(models.Model)
user_id = models.AutoField(primary_key=True)
listing_id = models.AutoField(primary_key=True)
booking_id = models.AutoField(primary_key=True)
rating =models.intager()
comment =models.CharField(max_length=10)
created_at =models.DateTimeField(auto_now_add=True)
def __str__(self):
    return self.name
 



























