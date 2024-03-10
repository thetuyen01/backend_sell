from django.contrib import admin
from .models import Invoice, Invoice_detail

# Register your models here.
@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'total_amount', 'address', 'phone_number', 'condition', 'created_at')
    list_filter = ('condition', 'created_at')
    search_fields = ('fullname', 'address', 'phone_number')

@admin.register(Invoice_detail)
class InvoiceDetailAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'product', 'quantity', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('invoice__fullname', 'product__name')

