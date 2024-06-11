from rest_framework import serializers

from products.models import Product

class ProductSerializers(serializers.HyperlinkedModelSerializer):
    name=serializers.ReadOnlyField()
    class Meta:
        model=Product
        fields='__all__'