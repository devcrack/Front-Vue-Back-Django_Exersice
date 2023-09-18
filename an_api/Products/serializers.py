# 3rd-party
from rest_framework import serializers
# Local
from Products.models import (Category,
                             InventoryRegister,
                             Product)


class CategoryModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class InventoryModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = InventoryRegister
        fields = '__all__'


class DetailProductReprModelSerializer(serializers.ModelSerializer):
    category = CategoryModelSerializer(many=False)

    class Meta:
        model = Product
        exclude = ['deleted']


class ProductReprModelSerializer(DetailProductReprModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'category']


class ProductCreatorModelSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=False, required=True)

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'category']

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












