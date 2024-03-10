from django.db import models
from products.models import Product


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    rating = models.IntegerField(default=0)
    image = models.ImageField(upload_to='upload_images/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
