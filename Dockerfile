# Usa la imagen base de Python 3.11 slim-bullseye
FROM python:3.11-slim-bullseye

# Establece las variables de entorno para Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Instala las dependencias del sistema y las bibliotecas necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    build-essential \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Crea y establece el directorio de trabajo
WORKDIR /code

# Copia los archivos de requisitos primero para aprovechar la cache de Docker
COPY requirements/requirements_api.txt /code/requirements_api.txt

# Actualiza pip e instala las dependencias de la aplicación, incluyendo psycopg2
RUN pip install --upgrade pip && \
    pip install -r /code/requirements_api.txt --no-cache-dir && \
    pip install psycopg2 --no-cache-dir


# Copia el código de la aplicación al contenedor
COPY . /code

# Establece las variables de entorno para la aplicación
ENV DATABASE_URL=postgresql://fyp_db_tsgh_user:8dq1LsgApzt6KMggLqY8p2ru3r3O09oy@dpg-cqkco1rqf0us73c7bm90-a.oregon-postgres.render.com/fyp_db_tsgh \
    DJANGO_CONFIGURATION=Production

# Descomenta las siguientes líneas si es la primera vez que se conecta a la base de datos
RUN python manage.py makemigrations && \
     python manage.py migrate && \
     python manage.py collectstatic --noinput && \
     python manage.py loaddata backup.json

# Expone el puerto de la aplicación
EXPOSE 8000

# Comando para iniciar el servidor de desarrollo
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--insecure"]

# Instrucciones para construir y ejecutar el contenedor
# Para construir -> docker build -f Dockerfile -t server . --no-cache
# Para ejecutar -> docker run --env-file .env -p 8000:8000 server



