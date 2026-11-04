from billing.models import Cliente, Factura, Cobro
from datetime import timedelta
from decimal import Decimal
from django.utils import timezone
from django.db.models import F


# UD3.6: operación 1, obtener todos los clientes.
def get_clientes_all():
    return Cliente.objects.all()

# UD3.6: operación 2, obtener las tres primeras facturas.
def get_factura_first_3():
    return Factura.objects.all()[:3]

# UD3.6: operación 3, facturas con total cero.
def get_factura_0():
    return Factura.objects.filter(total=0)


# UD3.6: operación 4, excluir clientes cuyo NIF empieza por 74.
def get_cliente_not_0612():
    return Cliente.objects.exclude(nif__startswith="74")

# UD3.6: operación 5, buscar por NIF y apellido.
def get_cliente_dni_apellido():
    return Cliente.objects.filter(
        nif="92436593F",
        apellidos__icontains="Pérez",
    )

# UD3.6: operación 6, facturas con id menor que 2.
def get_cli_id_lt_2_num_fact_des():
    return Factura.objects.filter(id__lt=2).order_by("-numero_factura")

# UD3.6: operación 7, clientes con id mayor que 2.
def get_cli_id_gt_2():
    return Cliente.objects.filter(id__gt=2)

# UD3.6: operación 8, facturas cuyo concepto contiene PHP.
def get_fact_des_nom_des():
    return Factura.objects.filter(
        concepto__icontains="PHP"
    ).order_by("numero_factura")

# UD3.6: operación 9, excluir facturas cuyo número termina en 1.
def get_fact_not_1():
    return Factura.objects.exclude(numero_factura__endswith="1")

# UD3.6: operación 10, primer cobro de una factura sobre Python.
def get_cobro_python_id2():
    return Cobro.objects.filter(
        factura__concepto__icontains="python",
        id__endswith="2",
    ).first()

# UD3.6: operación 11, cobros de facturas 06 excepto clientes Manu.
def get_cobro_fact6_not_manu():
    return Cobro.objects.filter(
        factura__numero_factura__contains="06"
    ).exclude(
        factura__cliente__nombre__icontains="Manu"
    )

# UD3.6: operación 12, facturas de total mayor o igual que 5.
def get_fact_gt_5():
    return Factura.objects.filter(total__gte=5)

# UD3.6: operación 13, cobros con importe entre 5 y 10.
def get_cobro_5_10():
    return Cobro.objects.filter(importe__range=(5, 10))

# UD3.6: operación 14, crear un cliente.
def create_cliente():
    return Cliente.objects.create(
        nombre="Nuevo",
        apellidos="apellido1 apellido2",
        nif="12345678Z",
        email="nuevo@example.com",
    )

from datetime import timedelta
from decimal import Decimal
from django.utils import timezone


# UD3.6: operación 15, crear una factura para el cliente anterior.
def create_factura():
    cliente = Cliente.objects.get(nif="12345678Z")
    ayer = timezone.localdate() - timedelta(days=1) # timedelta... coge un dia para luego se reste

    return Factura.objects.create(
        cliente=cliente,
        numero_factura="ORM-001",
        concepto="Factura de prueba ORM",
        fecha=ayer,
        total=Decimal("100.00"),
    )

# UD3.6: operación 16, añadir texto al concepto de la última factura.
def update_last_factura():
    factura = Factura.objects.order_by("-id").first()

    if factura is None:
        return None

    factura.concepto += " (última)"
    factura.save(update_fields=["concepto"])
    return factura

# UD3.6: operación 17, duplicar determinados cobros.
def update_cobro_fact2_x2():
    return Cobro.objects.filter(
        factura__numero_factura__endswith="2"
    ).update(
        importe=F("importe") * 2 # f es para recoger el valor de ese campo en la db 
    )

# UD3.6: operación 18, reducir a la mitad determinados cobros.
def update_cobro_fact1_cligonz_div2():
    return Cobro.objects.filter(
        factura__numero_factura__endswith="1",
        factura__cliente__apellidos__icontains="González",
    ).update(
        importe=F("importe") * Decimal("0.5")
    )

# UD3.6: operación 19, eliminar cobros de facturas con total menor que 1.
def delete_cobro_fact_lt_1():
    return Cobro.objects.filter(factura__total__lt=1).delete()

# UD3.6: operación 20, eliminar cobros de clientes llamados Pablo.
def delete_cobro_cli_pablo():
    return Cobro.objects.filter(
        factura__cliente__nombre__icontains="Pablo"
    ).delete()



