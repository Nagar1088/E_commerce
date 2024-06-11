from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .models import CartItem
from .serializers import cartserializers
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('product_list')

class CartItemModelViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = cartserializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
