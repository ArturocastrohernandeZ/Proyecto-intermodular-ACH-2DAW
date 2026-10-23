# Pilates=Life

Sistema de reservas, notificaciones y facturación para un estudio de pilates clásico.

**Autor:** Arturo Castro Hernández  
**Proyecto:** Proyecto intermodular — 2.º DAW

## Descripción

Pilates=Life será una aplicación web para centralizar la gestión de un estudio de
pilates clásico. Permitirá consultar las clases disponibles, elegir una sesión con
un profesor concreto, reservar una plaza y recibir confirmaciones, recordatorios y
avisos de cambios por correo electrónico o Telegram.

También incorporará la gestión de clientes, la emisión de facturas básicas y el
registro de cobros. Su objetivo es sustituir la información dispersa entre agendas,
mensajes y registros manuales por un sistema organizado que reduzca duplicidades,
errores de aforo y dificultades de comunicación.

## Objetivos

- Ofrecer un calendario con actividades, profesores, horarios, precios y plazas disponibles.
- Permitir que cada cliente reserve, cancele y consulte sus propias reservas.
- Facilitar la elección de un profesor concreto al seleccionar una sesión.
- Controlar el aforo y evitar reservas duplicadas y solapamientos del profesorado.
- Enviar notificaciones con asunto y mensaje por correo electrónico o Telegram.
- Gestionar clientes, facturas, cobros parciales y saldos pendientes.
- Proporcionar una zona de administración protegida por roles y una interfaz adaptable a móvil y ordenador.

## Tecnologías previstas

La arquitectura del proyecto seguirá las tecnologías definidas en el anteproyecto de ClickUp:

| Área | Tecnologías | Uso previsto |
| --- | --- | --- |
| Backend | Python y Django | Lógica de negocio, autenticación, permisos y administración. |
| API | Django REST Framework | Comunicación entre el backend y el frontend mediante una API. |
| Frontend | React, JavaScript, HTML y CSS | Calendario, reservas y pantallas de gestión mediante una interfaz adaptable. |
| Base de datos | PostgreSQL | Almacenamiento relacional con las relaciones y restricciones del modelo. |
| Entorno de ejecución | Docker y Docker Compose | Organización de los servicios de frontend, backend y base de datos. |
| Notificaciones | SMTP y Telegram Bot API | Envío de correos y mensajes de confirmación, recordatorio y cambios. |
| Tareas programadas | Celery y Redis | Programación de recordatorios, envíos en segundo plano y control de reintentos. |
| Control de versiones | Git y GitHub | Seguimiento de cambios y alojamiento del repositorio. |
| Documentación | Markdown y ClickUp | Documentación del repositorio, anteproyecto y planificación. |

Las versiones concretas de las herramientas se fijarán al iniciar el desarrollo autorizado.

## Usuarios y administración

- **Cliente:** consultará las sesiones, elegirá profesor y gestionará sus propias reservas.
  Podrá consultar sus facturas y cobros y seleccionar su canal de notificación.
- **Profesor:** consultará las sesiones asignadas y las reservas correspondientes,
  con acceso a la información necesaria para impartir sus clases.
- **Administración:** gestionará clientes, profesores, categorías, actividades,
  sesiones, reservas, notificaciones, facturas y cobros.

La zona de gestión requerirá autenticación y permisos comprobados en el backend.
Cada cliente tendrá acceso únicamente a sus propios datos y documentos.

## Modelo de datos

El modelo inicial contempla estas entidades:

- **Usuario:** cuenta de autenticación y permisos.
- **Cliente:** datos personales, NIF y correo electrónico únicos, y preferencias de notificación.
- **Profesor:** perfil del docente y sus sesiones asignadas.
- **Categoria:** clasificación de actividades y subcategorías.
- **Actividad:** modalidad del catálogo, descripción, duración habitual y precio base.
- **SesionClase:** clase concreta con actividad, profesor, fecha, horario, aforo, precio y estado.
- **Reserva:** relación entre un cliente y una sesión, con fecha de creación y estado.
- **Notificacion:** destinatario, reserva opcional, asunto, mensaje, canal, fechas y estado de envío.
- **Factura:** cliente, número de factura, concepto, fecha y total.
- **Cobro:** factura, fecha e importe recibido.

La actividad se separará de la sesión programada: el cliente elegirá un profesor
al reservar una sesión impartida por ese docente. Cada factura podrá tener varios
cobros para admitir pagos parciales. Las relaciones protegidas conservarán los
clientes con facturas y las facturas con cobros.

El esquema E/R completo está incluido **como imagen** en el anteproyecto de ClickUp,
junto con los campos, las cardinalidades y las reglas principales del modelo.

## Alcance inicial

La propuesta cubrirá un único estudio, con reservas y cancelaciones, elección de
profesor, avisos, administración y facturación básica con registro de cobros.
El saldo pendiente se calculará como el total de la factura menos la suma de sus cobros.

Las pasarelas de pago, los bonos, las listas de espera, la contabilidad completa
y la facturación electrónica se considerarán posibles ampliaciones. El registro
de cobros reflejará pagos recibidos; no realizará cargos bancarios.

## Proyecto en ClickUp

- [Proyecto Pilates=Life en ClickUp](https://app.clickup.com/1500510000002060/v/li/1500510000012546/1500510000011916?pr=1500510000010531)
- [Anteproyecto de Pilates=Life y esquema E/R](https://app.clickup.com/1500510000002060/docs/1ampjurgd0c-552/1ampjurgd0c-52)

## Estado y aprobación

Este README recoge la propuesta del anteproyecto y las tecnologías previstas.

**Fecha límite de entrega del anteproyecto:** miércoles 28 de octubre de 2026.

El desarrollo de la aplicación comenzará únicamente después de obtener el visto
bueno del equipo docente al anteproyecto presentado.
