# orders/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderModelViewSet

router = DefaultRouter()
router.register(r'orders', OrderModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
