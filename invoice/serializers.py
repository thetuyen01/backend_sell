from rest_framework import serializers
from .models import Invoice, Invoice_detail
from products.models import Image, Product
class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice_detail
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

# từ đơn hàng lấy ra chi tiết đơn hàng
class ImageSerializer(serializers.ModelSerializer):
    name = serializers.CharField() 
    image = serializers.ImageField() 

    class Meta:
        model  = Image
        fields = ['name', 'image']

class ProductSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=True)
    class Meta:
        model  = Product
        fields = ['id','name','price', 'image','description','slug','created_at']

class GetInvoiceDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Invoice_detail
        fields = '__all__'

class InvoiceWithDetailsSerializer(InvoiceSerializer):
    invoice_details = serializers.SerializerMethodField()

    class Meta:
        model = Invoice
        fields = '__all__'

    def get_invoice_details(self, obj):
        invoice_details = Invoice_detail.objects.filter(invoice=obj)
        serializer = GetInvoiceDetailSerializer(invoice_details, many=True)
        return serializer.data
