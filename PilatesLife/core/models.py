from decimal import Decimal

from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone
from billing.models import Cliente

# UD3.3a: modelo Profesor.
class Profesor(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,)
    nombre = models.CharField(max_length=256)
    apellidos = models.CharField(max_length=512)
    especialidad = models.CharField(max_length=256, blank=True)

    # UD3.4e: nombres visibles del modelo.
    class Meta:
        verbose_name = "profesor"
        verbose_name_plural = "profesores"

        # UD3.4f: ordenación por apellidos y nombre.
        ordering = ("apellidos", "nombre")

    # UD3.3b: representación textual de Profesor.
    def __str__(self):
        return f"{self.nombre} - {self.apellidos}"


# UD3.3a: modelo Categoria.
class Categoria(models.Model):
    categoria_padre = models.ForeignKey("self", on_delete=models.PROTECT, null=True, blank=True, related_name="subcategorias",)
    nombre = models.CharField(max_length=256)
    descripcion = models.TextField()

    # UD3.4e: nombres visibles del modelo.
    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"

        # UD3.4f: ordenación por nombre.
        ordering = ("nombre",)

    # UD3.3b: representación textual de Categoria.
    def __str__(self):
        return self.nombre

# UD3.3a: modelo Actividad.
class Actividad(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=256)
    descripcion = models.TextField()
    duracion_minutos = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    precio_base = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal("0.00"))])

    # UD3.3c: nombre único dentro de cada categoría.
    class Meta:
        unique_together = (("categoria", "nombre"),)

        # UD3.3a: duración positiva y precio no negativo.
        constraints = [models.CheckConstraint(condition=models.Q(duracion_minutos__gt=0), name="core_actividad_duracion_positiva",),  
                       models.CheckConstraint(condition=models.Q(precio_base__gte=0), name="core_actividad_precio_no_negativo",),]

        # UD3.4e: nombres visibles del modelo.
        verbose_name = "actividad"
        verbose_name_plural = "actividades"

        # UD3.4f: ordenación por nombre.
        ordering = ("nombre",)

    # UD3.3b: representación textual de Actividad.
    def __str__(self):
        return self.nombre

# UD3.3a: modelo SesionClase.
class SesionClase(models.Model):  
    
    class Estado(models.TextChoices):
        PROGRAMADA = "programada", "Programada"
        CANCELADA = "cancelada", "Cancelada"
        FINALIZADA = "finalizada", "Finalizada" 
    
    
    actividad = models.ForeignKey(Actividad, on_delete=models.PROTECT)
    profesor = models.ForeignKey(Profesor, on_delete=models.PROTECT)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    aforo = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    estado = models.CharField(max_length=10, choices=Estado.choices, default=Estado.PROGRAMADA)

    # UD3.3a: reglas de fechas, aforo y precio de la sesión.
    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=models.Q(fecha_fin__gt=models.F("fecha_inicio")),
                name="core_sesion_fin_posterior",
            ),
            models.CheckConstraint(
                condition=models.Q(aforo__gt=0),
                name="core_sesion_aforo_positivo",
            ),
            models.CheckConstraint(
                condition=models.Q(precio__gte=0),
                name="core_sesion_precio_no_negativo",
            ),
        ]

        # UD3.4e: nombres visibles del modelo.
        verbose_name = "sesión de clase"
        verbose_name_plural = "sesiones de clase"

        # UD3.4f: ordenación por fecha de inicio.
        ordering = ("fecha_inicio",)

    # UD3.3b: representación textual de SesionClase.
    def __str__(self):
        return f"{self.actividad} - {self.fecha_inicio} - {self.profesor}"

# UD3.3a: modelo Reserva.
class Reserva(models.Model):

    class Estado(models.TextChoices):
        CONFIRMADA = "confirmada", "Confirmada"
        CANCELADA = "cancelada", "Cancelada"
    
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    sesion = models.ForeignKey(SesionClase, on_delete=models.PROTECT)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    estado = models.CharField(max_length=10, choices=Estado.choices, default=Estado.CONFIRMADA)

    # UD3.3c: una reserva confirmada por cliente y sesión.
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["cliente", "sesion"],
                condition=models.Q(estado="confirmada"),
                name="core_reserva_confirmada_unica",
            ),
        ]

        # UD3.4e: nombres visibles del modelo.
        verbose_name = "reserva"
        verbose_name_plural = "reservas"

        # UD3.4f: ordenación por fecha de creación descendente.
        ordering = ("-fecha_creacion",)

    # UD3.3b: representación textual de Reserva.
    def __str__(self):
        return f"{self.cliente} - {self.sesion} - ({self.estado})"

# UD3.3a: modelo Notificacion.
class Notificacion(models.Model):

    class Canal(models.TextChoices):
        CORREO = "correo","Correo"
        TELEGRAM = "telegram", "Telegram"

    class Estado(models.TextChoices):
        PENDIENTE = "pendiente", "Pendiente"
        ENVIADA = "enviada", "Enviada"
        FALLIDA = "fallida", "Fallida"


    
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    reserva = models.ForeignKey(Reserva, null=True, blank=True, on_delete=models.PROTECT)
    asunto = models.CharField(max_length=255)
    mensaje = models.TextField()
    canal = models.CharField(max_length=8, choices=Canal.choices, default=Canal.CORREO)
    fecha_programada = models.DateTimeField(blank=True, null=True)
    fecha_envio = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=9, choices=Estado.choices, default=Estado.PENDIENTE)

    # UD3.4e: nombres visibles del modelo.
    class Meta:
        verbose_name = "notificación"
        verbose_name_plural = "notificaciones"

        # UD3.4f: ordenación por fecha programada descendente.
        ordering = ("-fecha_programada",)

    # UD3.3b: representación textual de Notificacion.
    def __str__(self):
        return f"{self.cliente} - {self.reserva} - {self.asunto} - ({self.estado})"
