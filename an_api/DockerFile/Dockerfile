FROM python:3.10
LABEL authors="Jesus Aurelio Hernandez"



# Establece las variables de entorno para evitar mensajes de advertencia de Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Crea y establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt /app/

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

# Copia todo el contenido del directorio actual al contenedor en /app/
COPY . /app/

# Puerto en el que se ejecutará la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación cuando se inicie el contenedor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
