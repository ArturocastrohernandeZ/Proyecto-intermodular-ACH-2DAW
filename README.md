# Sistema de Reservas

Aplicación web para consultar disponibilidad y gestionar reservas. El objetivo es
sustituir las reservas manuales por un sistema sencillo y organizado.

En el **Hito 1** se prepara únicamente la base del proyecto: Django arranca,
React consulta un endpoint de prueba y muestra su respuesta. Todavía no hay
funcionalidades de reservas, registro ni inicio de sesión.

## Tecnologías elegidas

- **Python y Django:** organización del backend y gestión de peticiones.
- **React y Vite:** interfaz mediante componentes y servidor de desarrollo.
- **CSS:** diseño sencillo y adaptable a móviles.
- **Supabase / PostgreSQL:** será la base de datos del sistema de reservas.
  Su conexión y configuración se implementarán más adelante.
- **Git y Markdown:** control de versiones y documentación.

La propuesta inicial y los motivos completos están en [Hito 0](docs/hito0.md).

## Estructura

```text
backend/           Django y endpoint de prueba
frontend/          React con Vite
docs/              Documentación y capturas de funcionamiento
.env.example       Variables de ejemplo, sin secretos
.gitignore         Exclusiones de Git
README.md          Instrucciones de arranque
```

## Arranque local

Los siguientes comandos están preparados para **PowerShell en Windows**.
Necesitas **Git**, **Python 3.11.9** y **Node.js 24 LTS con npm** instalados.
Puedes conseguirlos en [Python](https://www.python.org/downloads/)
y [Node.js](https://nodejs.org/en/download). Abre una terminal nueva tras instalarlos.

### 1. Clonar el repositorio

```powershell
git clone https://github.com/ArturocastrohernandeZ/Proyecto-intermodular-ACH-2DAW.git
cd Proyecto-intermodular-ACH-2DAW
```

Si ya tienes el proyecto descargado, abre la terminal en su carpeta raíz.

### 2. Configurar las variables de entorno

```powershell
Copy-Item .env.example .env
python backend/configure_env.py
```

Haz la copia solo la primera vez: sobrescribiría un `.env` existente.
El script genera una clave aleatoria local y la escribe directamente en `.env`,
sin mostrarla. Si ya hay una clave, la conserva.

| Variable | Qué debes poner |
| --- | --- |
| `DJANGO_SECRET_KEY` | La genera el script. No la publiques ni la copies en capturas. |
| `DJANGO_DEBUG` | `True` para esta prueba local. |
| `DJANGO_ALLOWED_HOSTS` | `localhost,127.0.0.1` para acceder desde tu equipo. |
| `BACKEND_URL` | `http://127.0.0.1:8000`, dirección del backend para el proxy de Vite. |

No hacen falta claves de Supabase para este hito.

### 3. Instalar las dependencias

Desde la raíz, prepara el backend:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r backend/requirements.txt
```

Después instala el frontend y vuelve a la raíz:

```powershell
cd frontend
npm.cmd ci
cd ..
```

No hace falta activar el entorno virtual: los comandos usan su Python directamente.

### 4. Base de datos (implementación pendiente)

Usaremos **Supabase con PostgreSQL**, pero su integración se realizará más adelante.
En este hito no hace falta configurar una base de datos ni ejecutar migraciones
o seeders: el endpoint de prueba devuelve una respuesta fija y no consulta datos.

### 5. Arrancar el backend

En una terminal situada en la raíz:

```powershell
.\.venv\Scripts\python.exe backend/manage.py runserver 127.0.0.1:8000
```

Déjala abierta. El backend queda en **http://127.0.0.1:8000/**.

- `/` devuelve `hola mundo`.
- `/api/health/` devuelve `{"status": "ok"}` con código HTTP 200.

La respuesta JSON se genera con Django directamente; no necesita Django REST Framework.

### 6. Arrancar el frontend

Abre **otra terminal**, también en la raíz:

```powershell
cd frontend
npm.cmd run dev
```

Déjala abierta. El frontend queda en **http://127.0.0.1:5173/**.
Pulsa `Ctrl+C` en cada terminal cuando quieras detener los servidores.

### 7. Comprobar que funciona

1. Abre http://127.0.0.1:8000/api/health/ y comprueba la respuesta JSON.
2. Abre http://127.0.0.1:5173/ y comprueba que aparece
   **«Conexión correcta con el backend»** y la respuesta recibida.
3. Pulsa **«Comprobar de nuevo»** para repetir la petición.

React solicita `/api/health/` al servidor Vite. Su proxy reenvía la petición
a Django en el puerto 8000 y devuelve la respuesta al navegador.
Este proxy es para desarrollo local; el despliegue se preparará en otro hito.

Para comprobar la compilación del frontend:

```powershell
cd frontend
npm.cmd run build
cd ..
```

## Dependencias y secretos

**No se suben a Git** `.venv/`, `node_modules/`, `.env`, bases de datos locales,
claves privadas ni archivos compilados. Las capturas tampoco deben mostrar secretos.

**Sí se incluyen** `requirements.txt`, `package.json`, `package-lock.json` y
`.env.example`: describen cómo preparar el entorno, sin incluir las dependencias
instaladas ni las credenciales reales.

No pongas secretos en variables con el prefijo `VITE_`: Vite las puede exponer
al navegador. El frontend no necesita la clave de Django.

Antes de subir cambios, revisa `git status` y los archivos seleccionados.
`.gitignore` no protege un secreto que ya haya sido añadido anteriormente a Git.

## Documentación y trabajo con Git

La instalación, las capturas y los problemas resueltos están en
[docs/instalacion.md](docs/instalacion.md).

Se utiliza `main` para la versión estable y `develop` para desarrollo.
Las funcionalidades pueden trabajarse en ramas `feature/...` y las correcciones
en `fix/...`. Los commits deben describir los cambios reales y cada integrante
debe realizar sus propias contribuciones.

Antes de la entrega, otro equipo debe clonar el repositorio y seguir este README.
El repositorio de GitHub debe estar actualizado y ser accesible para el profesor.
