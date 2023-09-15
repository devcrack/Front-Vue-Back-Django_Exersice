# std-lib
import uuid
# Django
from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.utils.translation import gettext_lazy as _
# Local
from UserProfile.managers import CustomUserManager
from Branches.models import Branch


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True)
    # Overriding email field
    email = models.EmailField(_("email address"), blank=False, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    # Using a custom query manager for this model
    """
    En el código Django, objects se ve como un atributo, pero en realidad es un descriptor especial que se utiliza para 
    realizar consultas en la base de datos asociadas al modelo. Este descriptor se utiliza principalmente para realizar 
    consultas en el modelo y no es un campo de la tabla de la base de datos.

Django utiliza esta convención para proporcionar un acceso sencillo y coherente a las operaciones de consulta en 
los modelos. Cuando se llama a métodos de consulta como all(), filter(), get(), etc., se hace a través de 
este descriptor objects. El descriptor objects se asocia al administrador de consultas que has definido para el modelo 
y permite realizar consultas en la tabla correspondiente a ese modelo en la base de datos.

En resumen, objects es un atributo especial de un modelo en Django que actúa como un descriptor para el administrador 
de consultas predeterminado del modelo y se utiliza para realizar operaciones de consulta en la base de datos. 
No es un campo de la tabla en la base de datos ni un método en el modelo en el sentido tradicional."""
    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email}"
