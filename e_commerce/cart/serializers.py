from rest_framework import serializers
from cart.models import  CartItem

class cartserializers(serializers.HyperlinkedModelSerializer):
     product=serializers.ReadOnlyField()
     class Meta:
          model=CartItem
          fields='__all__'
