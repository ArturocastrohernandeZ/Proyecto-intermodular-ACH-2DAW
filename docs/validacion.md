# Validación local del Hito 1

Comprobaciones realizadas el **7 de octubre de 2026** en Windows.

## Entorno utilizado

| Herramienta | Versión |
| --- | --- |
| Python | 3.11.9 |
| Django | 5.2.18 |
| Node.js | 24.21.0, copia portátil oficial temporal |
| React | 19.3.0 |
| Vite | 8.3.3 |

Las versiones instalables quedan fijadas en `backend/requirements.txt`
y `frontend/package-lock.json`. Las herramientas del navegador utilizadas para
estas comprobaciones se instalaron fuera del repositorio.

## Resultados

- `manage.py check`: sin problemas.
- `pip check`: sin incompatibilidades entre dependencias.
- Instalación del backend desde `requirements.txt`: correcta.
- Instalación del frontend con `npm.cmd ci`: correcta desde el archivo de bloqueo.
- `GET /`: HTTP 200 y texto `hola mundo`.
- `GET /api/health/`: HTTP 200 y JSON `{"status": "ok"}`.
- Compilación con `npm.cmd run build`: correcta.
- Chrome real: React recibió el JSON a través del proxy de Vite y mostró la conexión correcta.
- Fallo simulado del endpoint: la interfaz mostró un error comprensible.
- Reintento después del fallo: la interfaz volvió a mostrar la conexión correcta.
- Vista móvil de 390 píxeles: sin desbordamiento horizontal.
- Capturas del backend, frontend y móvil guardadas en `docs/capturas/`.
- Git ignora `.env`, `.venv/`, `node_modules/`, `dist/` y los archivos de datos locales.
- La clave local de Django no aparece en los archivos publicables ni en la compilación del frontend.

## Límites de esta validación

La prueba se realizó en este equipo; aún debe hacerse la revisión cruzada
desde un clon en otro equipo. No se ha preparado un despliegue de producción
ni conectado Supabase. Usaremos Supabase/PostgreSQL y su integración se implementará
más adelante. Las contribuciones de otros integrantes y la publicación
de la entrega en GitHub deben realizarse por sus responsables.
