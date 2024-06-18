# Etapa de construcción para clonar el repositorio y establecer la rama develop
FROM python:3.11-slim-bullseye

# Instala git
RUN apt-get update && apt-get install -y git

# Clona el repositorio
RUN git clone --branch develop https://github.com/FixYourPlants/fyp-api.git /code

# Establece el directorio de trabajo
WORKDIR /code



# Instala las dependencias de la aplicación
RUN pip install -r ./requirements.txt

# Ejecuta los siguientes comandos al iniciar el contenedor
RUN python manage.py makemigrations && \
    python manage.py migrate && \
    python manage.py loaddata ./backup.json

# Exponer el puerto
EXPOSE 8000

# Comando para iniciar el servidor de desarrollo
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

