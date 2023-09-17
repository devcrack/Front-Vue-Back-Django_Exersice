from django.contrib import admin
from .models import CustomUser
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ['email', 'role']
    search_fields = ['first_name', 'last_name', 'email']

    def role(self, user):
        if user.is_staff:
            return "staff"
        user_group = user.groups.all()
        if user_group:
            return user_group.first().name
        return ""



admin.site.register(CustomUser, UserProfileAdmin)


