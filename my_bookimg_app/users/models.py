from django.db import models
class user(models.Model):
user_name =models.CharField(max_length=100)
email =models.EmailField(unique=True)
password =models.CharField(max_length=100)
is_active =models.BooleanField(default=True)
created_at =models.DateTimeField(auto_now_add=True)
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

