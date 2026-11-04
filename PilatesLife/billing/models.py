from django.db import models

from django.utils import timezone
# UD3.3a: modelo Cliente.
class Cliente(models.Model):
    nombre = models.CharField(max_length=256)
    apellidos = models.CharField(max_length=512)
    nif = models.CharField(max_length=20)
    email = models.EmailField()

    # UD3.3c: NIF y correo únicos.
    class Meta:
        unique_together = (("nif",), ("email",))

        # UD3.4e: nombres visibles del modelo.
        verbose_name = "cliente"
        verbose_name_plural = "clientes"

        # UD3.4f: ordenación por apellidos y nombre.
        ordering = ("apellidos", "nombre")

    # UD3.3b: representación textual de Cliente.
    def __str__(self):
        return f"{self.nombre} {self.apellidos} ({self.nif})"

# UD3.3a: modelo Factura.
class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    numero_factura = models.CharField(max_length=20)
    concepto = models.TextField()
    fecha = models.DateField(default=timezone.localtime)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # UD3.3c: número de factura único.
    class Meta:
        unique_together = (("numero_factura",))

        # UD3.4e: nombres visibles del modelo.
        verbose_name = "factura"
        verbose_name_plural = "facturas"

        # UD3.4f: ordenación por número de factura.
        ordering = ("numero_factura",)

    # UD3.3b: representación textual de Factura.
    def __str__(self):
        return  f"{self.cliente} - {self.numero_factura}"

# UD3.3a: modelo Cobro.
class Cobro(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.PROTECT)
    fecha = models.DateField(default=timezone.now)
    importe = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # UD3.4e: nombres visibles del modelo.
    class Meta:
        verbose_name = "cobro"
        verbose_name_plural = "cobros"

        # UD3.4f: ordenación por fecha descendente.
        ordering = ("-fecha",)

    # UD3.3b: representación textual de Cobro.
    def __str__(self):
        return f"{self.factura.numero_factura} - {self.importe}"


