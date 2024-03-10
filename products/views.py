from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .models import Product
from event.models import Event
from event.serializers import EventSerializer

class ProductAPIView(APIView):
    def get(self, request):
        try:
            products = Product.objects.all()
            sz = ProductSerializer(products, many=True)
            return Response({
                "data":sz.data,
                "status":True
            },status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "messages":str(e),
                "status":False
            },status=status.HTTP_400_BAD_REQUEST)

class DetailProductAPIView(APIView):
    def get(self, request, id):
        try:
            product = Product.objects.get(id=id)
            sz = ProductSerializer(product)
            return Response({
                "data":sz.data,
                "status":True
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "messages":str(e),
                "status":False
            },status=status.HTTP_400_BAD_REQUEST)
        

class DetailProductSlugAPIView(APIView):
    def get(self, request, slug):
        try:
            product = Product.objects.filter(slug=slug).first()
            sz = ProductSerializer(product)
            return Response({
                "data":sz.data,
                "event":EventSerializer(Event.objects.all(), many=True).data,
                "status":True
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "messages":str(e),
                "status":False
            },status=status.HTTP_400_BAD_REQUEST)