# 3rd-party
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
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
                       'GET': ['manager', 'worker', 'consumer']}


class CategoryView(ProductBaseView):
    serializer_class = CategoryModelSerializer
    queryset = Category.objects.all()


class ProductView(ProductBaseView):
    serializer_class = ProductModelSerializer


class InventoryView(ProductBaseView):
    serializer_class = InventoryModelSerializer



