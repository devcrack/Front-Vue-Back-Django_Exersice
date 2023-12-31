from django.db import migrations
from django.contrib.auth.models import Group


def create_user_profiles_with_groups(apps, schema_editor):
    """
        This custom migration creates predefined user groups in the database.
        Groups are used to assign permissions and roles to users.

        Group names are defined in the group_names list and are created if they do not exist.
    """
    group_names = ['manager', 'worker', 'consumer']

    for group_name in group_names:
        Group.objects.get_or_create(name=group_name)


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_user_profiles_with_groups),
    ]
