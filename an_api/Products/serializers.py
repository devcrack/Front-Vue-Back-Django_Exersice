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
