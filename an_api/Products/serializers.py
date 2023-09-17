# 3rd-party
from rest_framework.serializers import ModelSerializer
# Local
from Products.models import (Category,
                             InventoryRegister,
                             Product)


class CategoryModelSerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class InventoryModelSerializer(ModelSerializer):

    class Meta:
        model = InventoryRegister


class ProductModelSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        stock = validated_data.get('stock', 0)
        instance = super().create(validated_data)
        if stock:
            InventoryRegister.objects.create(product=instance, quantity=stock, tipo='entry')

        return instance

