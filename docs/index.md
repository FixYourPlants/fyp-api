# Introducción

Este proyecto tiene como objetivo el desarrollo de una aplicación móvil llamada **FixYourPlants** que integra inteligencia artificial y una amplia base de conocimientos para realizar un análisis inmediato de la especie y enfermedad de las plantas, ofreciendo un cuidado óptimo.

**FixYourPlants** brindará a los usuarios no registrados servicios de consulta sobre plantas y enfermedades, junto con orientación sobre sus cuidados. Para los usuarios registrados, la aplicación ofrecerá identificación de especies y enfermedades mediante IA, así como la posibilidad de llevar un seguimiento diario de sus plantas.

## Objetivos y Solución Propuesta

Los objetivos principales de este proyecto son:

1. Desarrollar una aplicación móvil para el cuidado de plantas.
2. Crear una IA capaz de reconocer especies y enfermedades de plantas.
3. Adquirir conocimientos en un campo de la informática no cubierto durante el grado.

Para lograr estos objetivos, primero será necesario familiarizarse con el entorno y las herramientas de desarrollo para aplicaciones Android. El aprendizaje adicional se llevará a cabo en paralelo con el desarrollo del proyecto.

Debido a incompatibilidades tecnológicas y para evitar sobrecargar la aplicación, se optará por una separación entre el frontend y el backend. El frontend contendrá la aplicación Android, mientras que el backend gestionará la base de datos y la IA entrenada. La comunicación entre ambos se realizará a través de una API.

## Estudio de Mercado

Previo al desarrollo, se realizó un estudio de mercado para evaluar los estándares de calidad y funcionalidad del sector. Se analizaron las cinco aplicaciones más populares similares a **FixYourPlants** en Google Play Store: Plantix, Agrio, Blossom, Flora y PictureThis.

### Matriz de Características

| Id  | Característica                           | Plantix | Agrio | Blossom | Flora | PictureThis | FixYourPlants |
|-----|-----------------------------------------|---------|-------|---------|-------|-------------|---------------|
| #01 | IA reconocimiento de especie de plantas | X       | -     | -       | X     | X           | X             |
| #02 | IA reconocimiento de enfermedades       | X       | X     | -       | -     | X           | X             |
| #03 | Sección tus plantas/Plantas favoritas   | X       | -     | -       | -     | X           | X             |
| #04 | Listado de plantas                      | X       | -     | -       | X     | -           | X             |
| #05 | Listado de enfermedades                 | X       | -     | -       | -     | -           | X             |
| #06 | Detalles de enfermedades                | X       | -     | -       | -     | -           | X             |
| #07 | Listado de plagas                       | X       | -     | -       | -     | -           | X             |
| #08 | Consejos de cultivo                     | X       | -     | -       | -     | -           | X             |
| #09 | Localización                            | X       | -     | -       | -     | -           | -             |
| #10 | Nivel de experiencia                    | X       | X     | X       | -     | -           | -             |
| #11 | Clima                                   | X       | -     | -       | -     | -           | -             |
| #12 | Comunidad                               | X       | -     | -       | -     | -           | -             |
| #13 | Idioma                                  | X       | X     | -       | -     | -           | X             |
| #14 | Notificaciones                          | X       | X     | X       | -     | X           | X             |
| #15 | Suscripciones                           | -       | X     | X       | -     | -           | -             |
| #16 | Asistencia expertos                     | -       | X     | -       | -     | X           | -             |
| #17 | Amigos (Feed)                           | -       | X     | -       | -     | -           | -             |
| #18 | Inicio sesión con Google                | -       | -     | -       | X     | -           | X             |
| #19 | Tutorial de uso                         | -       | -     | -       | X     | -           | X             |
| #20 | Logros                                   | -       | -     | -       | X     | -           | -             |
| #21 | Historial de búsqueda                   | -       | -     | -       | X     | X           | X             |
| #22 | Sección de noticias                     | -       | -     | -       | X     | -           | -             |
| #23 | Compra de libros                        | -       | -     | -       | -     | X           | -             |
| #24 | Diario de plantas                       | -       | -     | -       | -     | -           | X             |
| #25 | Opiniones                               | -       | -     | -       | -     | -           | X             |
| #26 | Detalles de las plantas                 | -       | -     | -       | -     | -           | X             |


