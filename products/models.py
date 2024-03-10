from django.db import models
from django.utils.text import slugify

# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='upload_images/', blank=True, null=True)

    def __str__(self):
        return str(self.name)

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField() 
    slug = models.SlugField(max_length=1000, unique=True, blank=True)
    image = models.ManyToManyField(Image, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)