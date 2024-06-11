from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import add_to_cart, CartItemModelViewSet

router = DefaultRouter()
router.register(r'cart', CartItemModelViewSet)

urlpatterns = [
    path('add_to_cart/<int:product_id>/', add_to_cart),
    path('', include(router.urls)),
]
