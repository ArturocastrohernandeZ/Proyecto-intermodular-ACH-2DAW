# Sistema de Reservas

## Descripción

Este proyecto consiste en el desarrollo de una aplicación web para gestionar un sistema de reservas de forma sencilla y organizada.

La aplicación permitirá a los usuarios consultar la disponibilidad y realizar reservas desde una interfaz web. También permitirá gestionar la información relacionada con las reservas y los usuarios.

El objetivo principal es sustituir procesos de reserva manuales por un sistema digital más rápido, cómodo y accesible.

El proyecto se desarrollará separando el frontend, el backend y la base de datos, facilitando así su organización y mantenimiento.

## Tecnologías

### Guía de estilo / diseño

Para el diseño de la aplicación utilizaremos **CSS** junto con los componentes creados en React.

Buscaremos una interfaz sencilla, limpia e intuitiva, de forma que los usuarios puedan consultar y realizar reservas fácilmente.

La aplicación tendrá un diseño responsive para poder utilizarse correctamente tanto desde ordenadores como desde dispositivos móviles.

### Backend

Para el backend utilizare **Python con Django**.

He elegido Python porque es un lenguaje que permite desarrollar aplicaciones de forma clara y organizada.

Django será el framework encargado de gestionar la lógica de la aplicación, las peticiones realizadas desde el frontend y la comunicación con la base de datos.

También me permitirá organizar el backend en diferentes aplicaciones y mantener separadas las distintas partes del proyecto.

### Frontend

Para desarrollar el frontend utilizare **React**.

React me permitirá crear la interfaz mediante componentes reutilizables. De esta forma podre separar elementos como formularios, reservas, usuarios y otros componentes de la aplicación.

Para preparar y ejecutar el proyecto React utilizare **Vite**, ya que ofrece un entorno de desarrollo sencillo y rápido.

El frontend será el encargado de comunicarse con el backend para consultar, crear, modificar o cancelar reservas.

### Base de datos

Utilizare **Supabase** como plataforma para gestionar la base de datos.

Supabase utiliza **PostgreSQL**, una base de datos relacional adecuada para nuestro proyecto, ya que tendre información relacionada entre sí, como usuarios y reservas.

Una base de datos relacional me permitirá mantener los datos organizados mediante tablas y establecer relaciones entre ellas.

Entre los principales datos que almacenaremos estarán:

- Usuarios.
- Reservas.
- Fechas y horarios.
- Información necesaria para gestionar la disponibilidad.

### Documentación

La documentación principal del proyecto se realizará utilizando **Markdown** dentro del repositorio.

El fichero `README.md` contendrá la información general del proyecto, las tecnologías utilizadas y las decisiones principales tomadas durante el desarrollo.

También podre utilizar la documentación generada para los diferentes servicios o endpoints del backend a medida que avance el proyecto.

### Librerías y dependencias

Durante el desarrollo utilizare diferentes librerías y dependencias necesarias para React y Django.

Entre las principales se encontrarán:

- **Django** para desarrollar el backend.
- **React** para desarrollar la interfaz.
- **Vite** para crear y ejecutar el proyecto frontend.
- Las dependencias necesarias para conectar Django con PostgreSQL/Supabase.
- Librerías adicionales para validación, autenticación o testing si son necesarias durante el desarrollo.

Las dependencias concretas se irán añadiendo conforme avance el proyecto.

### Control de versiones

Utilizare **Git** para controlar las diferentes versiones del proyecto y **GitHub** para almacenar el repositorio.

La rama principal del proyecto será:

`main`

Para desarrollar nuevas funcionalidades utilizare ramas separadas. Algunos ejemplos serían:

`feature/sistema-reservas`

`feature/login`

`feature/interfaz`

Para corregir errores podre utilizar ramas como:

`fix/error-reserva`

Los commits tendrán mensajes cortos y descriptivos que permitan identificar fácilmente los cambios realizados.

Ejemplos:

`feat: añadir formulario de reservas`

`fix: corregir validación de fecha`

`docs: actualizar README`

Cuando una funcionalidad esté terminada y comprobada, su rama podrá fusionarse con `main`.

## Estructura del proyecto

El proyecto estará dividido principalmente en dos partes:

- **Frontend:** aplicación desarrollada con React y Vite.
- **Backend:** aplicación desarrollada con Python y Django.

La información de usuarios y reservas será almacenada en PostgreSQL mediante Supabase.

Esta separación permitirá mantener el código más organizado y facilitará el desarrollo del proyecto.
