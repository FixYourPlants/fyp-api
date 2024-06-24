# Usa la imagen base de Python
FROM python:3.11-slim-bullseye

# Instala git
RUN apt-get update && apt-get install -y git

# Clona el repositorio
COPY . /code
# RUN git clone --branch develop https://github.com/FixYourPlants/fyp-api.git /code

# Establece el directorio de trabajo
WORKDIR /code

# Instala las dependencias de la aplicación
RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

#---- Descomentar si es la primera vez que se conecta a esa base de datos ----#

# Establece las variables de entorno
# ENV DATABASE_URL=postgres://fyp_db_7e93_user:I9I07eyb3tPV5w2b2kBo38Yt4kYrySYS@dpg-cppfqlg8fa8c739fch4g-a.oregon-postgres.render.com/fyp_db_7e93
# ENV DJANGO_CONFIGURATION=Production

# Ejecuta los siguientes comandos al iniciar el contenedor
RUN python manage.py makemigrations && \
     python manage.py migrate && \
#     python manage.py loaddata backup.json

#---- Descomentar si es la primera vez que se conecta a esa base de datos ----#

# Exponer el puerto
EXPOSE 8000

# Comando para iniciar el servidor de desarrollo y recopilar archivos estáticos
CMD ["sh", "-c", "python manage.py collectstatic --noinput && python manage.py runserver 0.0.0.0:8000 --insecure"]

# To build -> docker build -f Dockerfile -t server . --no-cache
# To run -> docker run --env-file .env -p 8000:8000 server


