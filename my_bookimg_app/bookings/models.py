from django.db import models
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

class review(models.Model)
user_id = models.AutoField(primary_key=True)
listing_id = models.AutoField(primary_key=True)
booking_id = models.AutoField(primary_key=True)
rating =models.intager()
comment =models.CharField(max_length=10)
created_at =models.DateTimeField(auto_now_add=True)
def __str__(self):
    return self.name
 