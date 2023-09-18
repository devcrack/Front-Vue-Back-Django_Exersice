from django.contrib import admin
from Products.models import (Category,
                             Product,
                             InventoryRegister)


class ProductAdmin(admin.ModelAdmin):
    model = Product
    search_fields = ['branch__name', 'category__name', 'name', 'stock']
    list_display = ['name', 'category', 'stock', 'active']

    def active(self, product):
        return not product.deleted


class InventoryRegisterAdmin(admin.ModelAdmin):
    model = InventoryRegister
    search_fields = ['product__name', 'type', 'register_date']
    list_display = ['product', 'type', 'register_date']
    ordering = ['register_date']

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    search_fields = ['name']


admin.site.register(Product, ProductAdmin)
admin.site.register(InventoryRegister, InventoryRegisterAdmin)
admin.site.register(Category, CategoryAdmin)



