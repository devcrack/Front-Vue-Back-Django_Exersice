# 3rd-party
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Local
from an_api.base_permissions import HasGroupPermission
from Products.models import (Category,
                             InventoryRegister,
                             Product)
from Products.serializers import (CategoryModelSerializer,
                                  InventoryModelSerializer,
                                  ProductModelSerializer)


class ProductBaseView(ModelViewSet):
    permission_classes = [IsAuthenticated, HasGroupPermission]
    required_groups = {'POST': ['manager', 'worker'],
                       'PUT': ['manager', 'worker'],
                       'DELETE': ['manager'],
                       'GET': ['manager', 'worker', 'consumer']}

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        previous_stock = instance.stock

        instance.deleted = True

        if previous_stock > 0:
            instance.stock = 0
            InventoryRegister.objects.create(product=instance, quantity=0, type='issue')
        instance.save()

        return Response({'message': 'Product was successfully deleted'})


class CategoryView(ProductBaseView):
    serializer_class = CategoryModelSerializer
    queryset = Category.objects.all()


class ProductView(ProductBaseView):
    serializer_class = ProductModelSerializer


class InventoryView(ProductBaseView):
    serializer_class = InventoryModelSerializer



