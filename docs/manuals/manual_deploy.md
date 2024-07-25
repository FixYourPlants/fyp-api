# Manual de Despliegue en Render

Este manual describe el proceso para desplegar un contenedor en Render.

## Configuración del Contenedor

Para desplegar el contenedor `alesanfel/fyp-api` en Render, sigue estos pasos:

1. Inicia sesión en tu cuenta de Render en el navegador web.
2. En el panel de control de Render, selecciona el servicio donde deseas desplegar el contenedor.
3. En la configuración del servicio, busca la sección para configurar el despliegue del contenedor.
4. Asegúrate de que la configuración incluya los siguientes pasos:
   - Utiliza la imagen del contenedor `alesanfel/fyp-api` desde Docker Hub.
   - Especifica las variables de entorno necesarias para tu aplicación, como se muestra en el archivo `.env`.
   - Configura los puertos necesarios para la aplicación, por ejemplo, el puerto 8000.
5. Guarda los cambios en la configuración del servicio.

## Variables de Entorno en Render

Para añadir las variables de entorno necesarias en Render, sigue estos pasos:

1. En el panel de control de Render, navega hasta la configuración del servicio donde desplegarás el contenedor.
2. Busca la sección de variables de entorno o configuración avanzada relacionada con el entorno de ejecución.
3. Añade las siguientes variables de entorno según sea necesario para tu aplicación (utiliza como referencia el archivo `.env`):

   - `DJANGO_SECRET_KEY`: Clave secreta utilizada por Django para la seguridad de la aplicación.
   - `DATABASE_URL`: URL de la base de datos PostgreSQL que la aplicación utilizará.
   - `DJANGO_ALLOWED_HOSTS`: Lista de hosts permitidos para la aplicación Django.
   - `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_USE_TLS`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`: Configuración del servidor SMTP para enviar correos electrónicos.
   - `DJANGO_CONFIGURATION`: Configuración de Django, como `Production` para entorno de producción.
   - `DEFAULT_FROM_EMAIL`: Dirección de correo electrónico predeterminada para enviar correos desde la aplicación.
   - `RENDER_EXTERNAL_HOSTNAME`: Nombre de host externo proporcionado por Render.
   - `DJANGO_PAGINATION_LIMIT`: Límite de paginación para resultados en la aplicación Django.
   - `TF_CPP_MIN_LOG_LEVEL`, `TF_ENABLE_ONEDNN_OPTS`: Configuración de TensorFlow para optimización y registros mínimos.

4. Guarda las variables de entorno configuradas en el servicio de Render.

## Ejecución del Despliegue

Una vez configurado, ejecuta el despliegue del contenedor en Render con los siguientes pasos:

1. Confirma que todos los ajustes están correctos en la configuración del servicio de Render.
2. Inicia el despliegue del servicio. Render manejará automáticamente la construcción y ejecución del contenedor.
3. Verifica el estado del despliegue en el panel de control de Render para asegurarte de que la aplicación esté activa y funcionando correctamente.
4. Accede a la URL proporcionada por Render para ver tu aplicación desplegada.

Este proceso completa el despliegue del contenedor `alesanfel/fyp-api` en Render. Asegúrate de seguir los pasos con cuidado para garantizar un despliegue exitoso de tu aplicación.

