# Bot de WhatsApp con Flask y SQLite

Un backend sencillo en Python para automatizar respuestas de WhatsApp y guardar los datos de los clientes que escriben pidiendo info. Lo armé para resolver el típico problema de los negocios locales que pierden clientes fuera de horario.

## Qué hace
- Responde automáticamente con un menú de opciones según lo que escriba el usuario.
- Guarda cada consulta (número, mensaje, opción elegida y hora) en una base de datos local en SQLite para que no se pierda ningún contacto.

## Tecnologías
- Python
- Flask
- SQLite3

## Cómo correrlo localmente

1. Clona el repositorio o descarga los archivos.
2. Instala Flask si no lo tienes:
   ```bash
   pip install flask