# 3rd-party
from django.urls import path
from rest_framework.routers import SimpleRouter
# Local
from Products.views import CategoryView, InventoryView, ProductView


router = SimpleRouter()

router.register(r'categories', CategoryView)
router.register(f'inventory-register', InventoryView)
router.register(f'product', ProductView)


urlpatterns = router.urls
