from django.shortcuts import render
from .models import Product
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializers

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product.html', {'products': products})


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
