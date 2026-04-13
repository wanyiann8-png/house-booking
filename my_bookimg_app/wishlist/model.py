from django.db import models
class wishlist_items(models.Model)
wishlist_id = models.AutoField(primary_key=True)
listing_id = models.AutoField(primary_key=True)
def __str__(self):
    return self.name

class wishlist(models.Model)
user_id = models.AutoField(primary_key=True)
name =models.CharField(max_length=100)
created_at =models.DateTimeField(auto_now_add=True)
def __str__(self):
    return self.name

