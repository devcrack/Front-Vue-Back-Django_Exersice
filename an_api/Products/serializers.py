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
            InventoryRegister.objects.create(product=instance, quantity=stock, type='entry')

        return instance

    def update(self, instance, validated_data):
        previous_stock = instance.stock
        new_stock = validated_data.get('stock', instance.stock)

        if previous_stock != new_stock:
            move_type = 'entry' if new_stock > previous_stock else 'issue'
            _quantity = abs(new_stock - previous_stock)
            InventoryRegister.objects.create(product=instance, quantity=_quantity, type=move_type)

        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.category = validated_data.get('category', instance.category)
        instance.stock = new_stock

        instance.save()

        return instance










