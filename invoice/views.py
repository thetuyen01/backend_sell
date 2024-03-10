from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import InvoiceSerializer, InvoiceDetailSerializer,InvoiceWithDetailsSerializer
from .models import Invoice
class InvoiceAPIView(APIView):
    def post(self, request):
        try:
            invoice = request.data 
            detail_invoice = request.data['data']
            invoice_obj = {
                "fullname": invoice['full_name'],
                "total_amount": invoice['total_amount'],
                "address": invoice['address'],
                "phone_number": invoice['phone_number'],
                "notes": "giaohangcanthan",
                "condition": 1
            }
            
            sz_invoice = InvoiceSerializer(data=invoice_obj)
            if not sz_invoice.is_valid():
                return Response({
                    "messages": sz_invoice.errors,
                    "status": False
                }, status=status.HTTP_400_BAD_REQUEST)
            
            sz_invoice.save()
            
            for item in detail_invoice:
                detail_obj = {
                    "invoice": int(sz_invoice.instance.id),
                    "product": int(item['id']),
                    "quantity": int(item['count'])
                }
                sz_detail = InvoiceDetailSerializer(data=detail_obj)
                
                if not sz_detail.is_valid():
                    return Response({
                        "messages": sz_detail.errors,
                        "status": False
                    }, status=status.HTTP_400_BAD_REQUEST)
                
                sz_detail.save()

            invoice_res = Invoice.objects.get(id = sz_invoice.instance.id)
            sz_res = InvoiceWithDetailsSerializer(invoice_res)

            return Response({
                "messages": "Success",
                "data":sz_res.data,
                "status": True
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({
                "messages": str(e),
                "status": False
            }, status=status.HTTP_400_BAD_REQUEST)

        