# 3rd-party
from django.urls import path, include
from rest_framework.routers import SimpleRouter
# Local
from Products.views import CategoryView, InventoryView, ProductView

router = SimpleRouter()

router.register(r'categories', CategoryView, basename='category')
router.register(f'products', ProductView, basename='product')

urlpatterns = [
    path(f'inventory-register/<uuid:product_pk>/', InventoryView.as_view({'get': 'list'}), name='inventory_register'),
    path('', include(router.urls)),
]


