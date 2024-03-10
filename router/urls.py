from django.urls import path
from products.views import ProductAPIView, DetailProductAPIView, DetailProductSlugAPIView
from invoice.views import InvoiceAPIView
urlpatterns = [
    path('products/', ProductAPIView.as_view()),
    path('products/<int:id>', DetailProductAPIView.as_view()),
    path('invoice/', InvoiceAPIView.as_view()),
    path('product/<slug:slug>', DetailProductSlugAPIView.as_view())
]