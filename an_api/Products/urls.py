# 3rd-party
from django.urls import path
from rest_framework.routers import SimpleRouter
# Local
from Products.views import CategoryView, InventoryView, ProductView


router = SimpleRouter()

router.register(r'categories', CategoryView, basename='category')
router.register(f'inventory-registers', InventoryView, basename='inventory-register')
router.register(f'products', ProductView, basename='product')


urlpatterns = router.urls
