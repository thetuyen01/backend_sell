from django.db import models
from products.models import Product
# Create your models here.
class Invoice(models.Model):
    fullname = models.CharField(max_length=200)
    total_amount = models.DecimalField(max_digits=10, decimal_places=3)
    address = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=100)
    notes = models.CharField(max_length=500)
    condition = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.fullname)
    
class Invoice_detail(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.invoice.fullname)