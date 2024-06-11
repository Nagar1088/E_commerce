from rest_framework import serializers
from orders.models import Order

class OrderSerializers(serializers.HyperlinkedModelSerializer):
    product=serializers.ReadOnlyField()
    class Meta:
        model=Order
        fields='__all__'