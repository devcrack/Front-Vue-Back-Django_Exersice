from django.contrib.auth.models import Group
from rest_framework import permissions


class HasGroupPermission(permissions.BasePermission):

    @staticmethod
    def __is_in_group(user, group_name):
        """
        Takes a user and a group name, and returns `True` if the user is in that group.
        """
        try:
            return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
        except Group.DoesNotExist:
            return False

    def has_permission(self, request, view) -> bool:
        required_groups_mapping = getattr(view, "required_groups", {})

        # Determine the required groups for this particular request method.
        required_groups = required_groups_mapping.get(request.method, [])
        if request.user.is_staff:
            return True
        for group_name in required_groups:
            press_f_for_respect = self.__is_in_group(request.user, group_name)
            if press_f_for_respect:
                return True
        return False
