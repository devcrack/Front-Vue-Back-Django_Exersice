# Frontend


# Backend
Para poner en funcionamiento este proyecto de Django, debes seguir estos pasos:

### Paso 1: Configurar el entorno de desarrollo

Asegúrate de tener Python y pip instalados en tu sistema. Si aún no los tienes, instálalos antes de continuar.

### Paso 2: Clonar el repositorio

Si estás utilizando un repositorio de control de versiones (por ejemplo, Git), clona el repositorio del proyecto en tu máquina local.

### Paso 3: Crear un entorno virtual (opcional pero recomendado)

Es una buena práctica crear un entorno virtual para aislar las dependencias del proyecto. 
Puedes usar la siguiente secuencia de comandos para crear y activar un entorno virtual:

```bash
python -m venv myenv  # Crea un entorno virtual llamado 'myenv'
source myenv/bin/activate  # Activa el entorno virtual (Linux/Mac)
```
### Paso 4: Instalar las dependencias

Instala las dependencias del proyecto utilizando pip. Asegúrate de estar en la raíz del proyecto donde se encuentra el 
archivo ```Test/an_api/requirements.txt```. Ejecuta el siguiente comando:

``` bash
pip install -r requirements.txt
```
Esto instalará todas las bibliotecas requeridas para el proyecto.

### Paso 5: Configurar la base de datos

Asegúrate de tener una base de datos configurada. En este proyecto, la configuración de la base de datos se obtiene del 
archivo ```local_config.json``` . Asegúrate de que este archivo esté presente en la raíz del 
proyecto ```Test/an_api/local_config.json``` y que contenga la configuración correcta de la base de datos.

#### Ejemplo contenido local_config.json
```json
{
  "DATABASES": {
    "default": {
      "ENGINE": "django.db.backends.postgresql",
      "NAME": "a_local_db",
      "USER": "tenma",
      "PASSWORD": "mientras123",
      "HOST": "localhost",
      "PORT": "5432"
    }
  },
  "EMAIL": {
    "EMAIL_BACKEND": "django.core.mail.backends.smtp.EmailBackend",
    "EMAIL_HOST": "smtp-relay.brevo.com",
    "EMAIL_USE_TLS": false,
    "EMAIL_PORT": 587,
    "EMAIL_HOST_USER": "my_user@mail.com",
    "EMAIL_HOST_PASSWORD": "my_password"
  }
}

```


### Paso 6: Aplicar las migraciones

Ejecuta las migraciones para crear las tablas de la base de datos y aplicar las configuraciones iniciales:

```bash
python manage.py makemigrations
python manage.py migrate
Paso 7: Crear un superusuario
```
Crea un superusuario para acceder al panel de administración de Django:

```bash
python manage.py createsuperuser
```
Sigue las instrucciones para configurar el nombre de usuario, correo electrónico y contraseña del superusuario.

### Paso 8: Ejecutar el servidor de desarrollo

Inicia el servidor de desarrollo de Django con el siguiente comando:

```bash
python manage.py runserver
```
El servidor se ejecutará en http://localhost:8000/ de forma predeterminada.

### Paso 9: Acceder al panel de administración y a la **Documentacion del API**

- Accede al panel de administración de Django ingresando en tu navegador http://localhost:8000/admin/ y usa las 
  credenciales del superusuario que creaste en el paso 7.

- Acceder a la documentacion del API ingresa en tu navegador: 
- http://127.0.0.1:8000/an_api/schema/redoc/
- http://127.0.0.1:8000/an_api/schema/swagger-ui/


## Ejecutar Pruebas

Desde el directorio Raiz del proyecto: ```an_api/```
ejecutar: ``pytest -s -v``
Esto ejecutara automaticamente las pruebas que se tengan escritas en el proyecto .
Si todo va bien tendremos una salida como la siguiente:
```bash
UserProfile/tests/test_user_profile.py::test_register_manager_user_should_succed Creating test database for alias 'default'...
PASSED
UserProfile/tests/test_user_profile.py::test_login_success PASSED
UserProfile/tests/test_user_profile.py::test_logout_success PASSED
UserProfile/tests/test_user_profile.py::test_get_user_detail_should_pass PASSEDDestroying test database for alias 'default'...


===================================================================================== 4 passed in 4.96s ======================================================================================


```

En caso de posibles errores hacer: 
``bash
export DJANGO_SETTINGS_MODULE=an_api.settings
``
Asi establecemos la variable de entorno  DJANGO_SETTINGS_MODULE con el 
valor an_api.settings. 
Esto le indica a Django cuál es el archivo de configuración de 
ajustes que debe cargar cuando se ejecuten comandos de 
Django desde la línea de comandos y en teoria deberiamos de poder ejecutar 
nuestras pruebas escritas con pytest sin ningun problema.


## Opcional Ejecutar Proyecto con Docker

Abre una terminal y navega al directorio que contiene tu proyecto Django y el Dockerfile.

Construye la imagen del contenedor utilizando el siguiente comando:

```bash
docker build -t an/api/DockerFile/DockerFile
```
Reemplaza nombre-de-la-imagen con un nombre adecuado para tu imagen.

Una vez que la imagen se haya construido correctamente, 
puedes ejecutar un contenedor basado en esa imagen con el 
siguiente comando:

```bash
docker run -p 8000:8000 nombre-de-la-imagen
```
Esto mapea el puerto 8000 del contenedor al puerto 8000 del host.

Tu proyecto Django debería estar ahora en funcionamiento 
en un contenedor Docker. Puedes acceder a él en tu navegador 
web utilizando http://localhost:8000/.

