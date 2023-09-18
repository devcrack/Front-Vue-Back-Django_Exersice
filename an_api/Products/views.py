# 3rd-party
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import (ModelViewSet,
                                     ReadOnlyModelViewSet)


# Local
from an_api.base_permissions import HasGroupPermission
from Products.models import (Category,
                             InventoryRegister,
                             Product)
from Products.serializers import (CategoryModelSerializer,
                                  DetailProductReprModelSerializer,
                                  InventoryModelSerializer,
                                  ProductCreatorModelSerializer,
                                  ProductReprModelSerializer,
                                  )


class ProductBaseView(ModelViewSet):
    permission_classes = [IsAuthenticated, HasGroupPermission]
    required_groups = {'POST': ['manager', 'worker'],
                       'GET': ['manager', 'worker', 'consumer']}


class CategoryView(ProductBaseView):
    serializer_class = CategoryModelSerializer
    queryset = Category.objects.all()


class ProductView(ProductBaseView):
    serializer_class = ProductCreatorModelSerializer
    required_groups = required_groups = {'POST': ['manager', 'worker'],
                                         'PUT': ['manager', 'worker'],
                                         'PATCH': ['manager', 'worker'],
                                         'DELETE': ['manager'],
                                         'GET': ['manager', 'worker', 'consumer']}
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductReprModelSerializer
        elif self.action == 'retrieve':
            return DetailProductReprModelSerializer
        return ProductCreatorModelSerializer

    def partial_update(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()(instance=self.get_object(),
                                                 data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Product Updated'}, status=status.HTTP_200_OK)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        prev_stock = instance.stock
        instance.deleted = True

        InventoryRegister.objects.create(product=instance, quantity=prev_stock, type='deleted')
        instance.stock = 0

        instance.save()

        return Response({'message': 'Product was successfully deleted'})


class InventoryView(ReadOnlyModelViewSet):
    serializer_class = InventoryModelSerializer

    permission_classes = [IsAuthenticated, HasGroupPermission]
    required_groups = {'GET': ['manager', 'worker', 'consumer']}

    def get_queryset(self):
        product_pk = self.kwargs.get('product_pk')
        product = Product.objects.filter(id=product_pk).first()

        if product:
            return product.InventoryRegister.all()
        # Returning an empty queryset
        return InventoryRegister.objects.none()

