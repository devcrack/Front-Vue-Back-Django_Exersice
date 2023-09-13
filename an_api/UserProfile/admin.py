from django.contrib import admin
from .models import CustomUser
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    model = CustomUser
    search_fields = ['first_name', 'last_name', 'email']


admin.site.register(CustomUser, UserProfileAdmin)


