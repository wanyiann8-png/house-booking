from django.db import models
class payments(models.Model)
payment_id = models.AutoField(primary_key=True)
amount =models.DecimalField(max_digits=7, decimal_places=5)
payment_method =models.CharField(max_length=100)
status =models.CharField(max_length=10)
transaction_ref =models.CharField(max_length=100)
created_at =models.DateTimeField(auto_now_add=True)
def __str__(self):
    return self.name