# Manual de Desarrollo

En este manual se describen los pasos necesarios para configurar correctamente el entorno de desarrollo de la aplicación. Para facilitar la comprensión, el manual se ha dividido en tres partes: backend, frontend e IA.

## Backend

La estructura del backend se organiza de la siguiente manera:

- **`app`**: Contiene el código fuente de la aplicación.
- **`docs`**: Incluye la documentación de la aplicación.
- **`media`**: Almacena las imágenes guardadas durante la interacción con el backend.
- **`backup.json`**: Contiene una versión estable de la base de datos.
- **`Dockerfile`**: Archivo utilizado para ejecutar la aplicación en un contenedor.

### Clonación del Repositorio

Para clonar el código fuente desde GitHub, utiliza el siguiente comando:

```bash
$ git clone https://github.com/FixYourPlants/fyp-api.git
```

### Configuración del Entorno

Agrega y configura el archivo `.env` según tus necesidades. Un ejemplo de configuración del archivo `.env` es el siguiente:

```
# Variables para el entorno de desarrollo
DJANGO_SECRET_KEY=%)*j%&wt_p(9e#t#2+9!uf@!8n3352q9e+!m%l4u)odmmusdc!
DATABASE_URL=postgres://fyp_db_7e93_user:I9I07eyb3tPV5w2b2kBo38Yt4kYrySYS@dpg-cppfqlg8fa8c739fch4g-a.oregon-postgres.render.com/fyp_db_7e93
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,10.0.2.2

# Variables para el entorno de producción
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=lennient.enterprise@gmail.com
EMAIL_HOST_PASSWORD=yltf khuu xjdk vrah

# Variables comunes (se usan tanto en desarrollo como en producción)
DJANGO_CONFIGURATION=Local

# Variables adicionales para el entorno de producción
DEFAULT_FROM_EMAIL=lennient.enterprise@gmail.com
RENDER_EXTERNAL_HOSTNAME=your_render_external_hostname

# Paginación
DJANGO_PAGINATION_LIMIT=10

TF_CPP_MIN_LOG_LEVEL=2
TF_ENABLE_ONEDNN_OPTS=0
```

### Entorno Local

Para configurar el entorno local, sigue estos pasos:

```python
$ pip install virtualenv
$ virtualenv --no-site-packages venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

### Docker

Si prefieres utilizar Docker, puedes construir y ejecutar el contenedor con los siguientes comandos:

```python
$ docker build -f Dockerfile -t server . --no-cache
$ docker run --env-file .env -p 8000:8000 server
```

## Frontend

La estructura del frontend en un proyecto de Android se organiza de la siguiente manera:

- **`app`**: Contiene el código fuente y los recursos del proyecto.
  - **`manifests`**: Contiene el archivo `AndroidManifest.xml`, que define la estructura básica del proyecto.
  - **`java`**: Contiene el código fuente en Kotlin del proyecto, organizado por paquetes:
    - **`data`**: Recursos necesarios para realizar las peticiones a las APIs.
    - **`ui`**: Componentes de la interfaz de usuario.
    - **`utils`**: Herramientas y utilidades para el desarrollo.
    - **`viewmodel`**: Clases del patrón de arquitectura MVVM (Model-View-ViewModel).
  - **`res`**: Recursos utilizados por el proyecto, tales como:
    - **`drawable`**: Imágenes y gráficos.
    - **`layout`**: Archivos de diseño en XML que definen la interfaz de usuario.
    - **`values`**: Archivos XML para valores como cadenas, estilos, colores, etc.
    - **`mipmap`**: Iconos de la aplicación en diferentes resoluciones.
    - **`raw`**: Archivos de recursos sin procesar, como archivos de audio o video.
  - **`assets`**: Archivos de recursos en bruto que se pueden acceder desde el código.
- **`build`**: Archivos y carpetas generados por el sistema de compilación.
- **`gradle`**: Archivos de configuración del sistema de compilación Gradle.
- **`.gitignore`**: Especifica qué archivos y directorios deben ser ignorados por el control de versiones Git.
- **`build.gradle (Project)`**: Archivo de configuración de Gradle para el proyecto en general.
- **`build.gradle (Module: app)`**: Archivo de configuración de Gradle específico para el módulo de la aplicación.
- **`settings.gradle`**: Especifica los módulos incluidos en el proyecto.

### Clonación del Repositorio

Para clonar el código fuente desde GitHub, utiliza Android Studio. Abre Android Studio y, en la pantalla de bienvenida, selecciona `Get from VCS`. En el campo `URL`, pega la URL del repositorio de GitHub, por ejemplo, `https://github.com/FixYourPlants/fyp-app.git`. Luego, selecciona el directorio donde deseas clonar el proyecto y haz clic en `Clone`.

### Configuración del Entorno

Una vez clonado el repositorio, Android Studio descargará el proyecto y abrirá automáticamente la ventana del proyecto. Debes esperar a que Android Studio configure el proyecto, lo cual puede incluir la sincronización de Gradle y la descarga de las dependencias necesarias.

A continuación, es necesario agregar el archivo `google_services.json`. Este archivo se debe descargar desde la consola de Firebase y colocarlo en la carpeta `app` del proyecto.

Después de agregar el archivo `google_services.json`, revisa los archivos `build.gradle` y asegúrate de que todas las dependencias estén correctamente configuradas. También es importante ajustar la configuración del SDK de Android si es necesario. Esto se puede hacer desde `File > Project Structure > SDK Location`, asegurándote de que el `Android SDK` esté apuntando al directorio correcto.

### Ejecución de la Aplicación

Finalmente, selecciona el dispositivo de destino o emulador en el que deseas ejecutar la aplicación. Haz clic en el botón `Run` (ícono de reproducción verde) o usa el atajo `Shift + F10`. Android Studio construirá el proyecto y desplegará la aplicación en el dispositivo o emulador seleccionado.

## IA

La estructura del proyecto de IA se organiza de la siguiente manera:

- **`datasets`**: Contiene los conjuntos de datos utilizados para entrenar y evaluar los modelos de IA. Los datos deben descargarse utilizando el archivo `downloads.py`.
- **`models`**: Almacena los modelos entrenados. Incluye el modelo entrenado en formato `.h5` en su última versión.
- **`tensorboard_logs`**: Contiene los registros de TensorBoard, utilizados para visualizar métricas de entrenamiento y evaluación.
- **`LICENSE.txt`**: Contiene la licencia bajo la cual se distribuye el proyecto. Define los términos y condiciones de uso, distribución y modificación del software.
- **`model_utility.py`**: Contiene funciones y utilidades auxiliares que facilitan el manejo de modelos, como funciones para cargar, guardar y evaluar modelos.
- **`PlantDoc_Examples.png`**: Proporciona ejemplos visuales relacionados con el proyecto, como ejemplos de datos de entrada o resultados de predicción.
- **`README.md`**: Proporciona una descripción general del proyecto, incluyendo su propósito, cómo configurarlo y cómo utilizarlo.
- **`requirements.txt`**: Lista todas las dependencias del proyecto, especificando las bibliotecas y versiones necesarias para ejecutar el código.
- **`downloads.py`**: Permite descargar el dataset que se utiliza para entrenar el modelo.
- **`train.ipynb`**: Este archivo Jupyter Notebook contiene el código y los pasos para entrenar el modelo de IA, incluyendo la carga de datos, el preprocesamiento, la definición del modelo, el entrenamiento y la evaluación.

### Clonación del Repositorio

Para clonar el código fuente del proyecto de IA desde GitHub, utiliza el siguiente comando:

```bash
$ git clone https://github.com/FixYourPlants/fyp-ai.git
```

### Configuración del Entorno

Después de clonar el repositorio, instala las dependencias listadas en el archivo `requirements.txt` mediante el siguiente comando:

```bash
$ pip install -r requirements.txt
```

A continuación, ejecuta el script downloads.py para descargar el conjunto de datos necesario para entrenar el modelo:

```bash
$ python downloads.py
```

Luego, accede al directorio `datasets` y ejecuta el script `move.py` para finalizar la configuración del entorno según las especificaciones dentro de ese archivo:

```bash
$ python move.py
```

### Ejecución del Entrenamiento

Abre el archivo `train.ipynb` con Jupyter Notebook o JupyterLab para revisar y ejecutar el proceso de entrenamiento del modelo de IA. Asegúrate de que todas las dependencias estén instaladas correctamente y de que los archivos de datos estén en su lugar para que el notebook funcione sin problemas.


