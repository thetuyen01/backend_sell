from django.contrib import admin
from .models import Product, Image


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'description')

admin.site.register([Image])

