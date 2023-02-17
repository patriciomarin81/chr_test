from django.db import models

# Create your models here.

#BIKE SANTIAGO
class payment(models.Model):
    id_payment = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50) 

class extra(models.Model):
    id_extra = models.AutoField(primary_key=True)
    address = models.CharField(max_length=200) 
    altitude = models.DecimalField(decimal_places=1, max_digits=12)
    ebikes = models.IntegerField()
    has_ebikes = models.BooleanField()
    last_updated = models.IntegerField()
    normal_bikes = models.IntegerField()
    payment = models.ManyToManyField(payment)
    payment_terminal = models.BooleanField()
    post_code = models.CharField(max_length=20) 
    renting = models.IntegerField()
    returning = models.IntegerField()
    slots = models.IntegerField()
    uid = models.CharField(max_length=20) 

class station(models.Model):
    empty_slots = models.IntegerField()
    extra = models.ForeignKey(extra, on_delete=models.CASCADE)
    free_bikes = models.IntegerField()
    id_station = models.CharField(max_length=200,primary_key=True) 
    latitude = models.DecimalField(decimal_places=1, max_digits=12)
    longitude = models.DecimalField(decimal_places=1, max_digits=12)
    name = models.CharField(max_length=200) 
    timestamp = models.CharField(max_length=200)

class company(models.Model):
    id_company = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200) 

class location(models.Model):
    id_location = models.AutoField(primary_key=True)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    latitude = models.DecimalField(decimal_places=1, max_digits=12)
    longitude = models.DecimalField(decimal_places=1, max_digits=12)

class network(models.Model):
    company = models.ManyToManyField(company)
    gbfs_href = models.CharField(max_length=200)
    href = models.CharField(max_length=200)
    id_network = models.CharField(max_length=200,primary_key=True)
    location = models.ForeignKey(location, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    stations = models.ManyToManyField(station) 


#SERVICIO DE EVALUACION AMBIENTAL

class titular(models.Model):
    id_titular = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=500)
    domicilio = models.CharField(max_length=500)
    ciudad = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    fax = models.CharField(max_length=50)
    email = models.CharField(max_length=100)

class representanteLegal(models.Model):
    id_titular = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=500)
    domicilio = models.CharField(max_length=500)
    telefono = models.CharField(max_length=50)
    fax = models.CharField(max_length=50)
    email = models.CharField(max_length=100)

class proyecto(models.Model):
    id_proyecto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=500)
    tipo_proyecto = models.CharField(max_length=500)
    monto_inversion = models.CharField(max_length=500)
    estado_actual = models.CharField(max_length=500)
    encargado = models.CharField(max_length=500)
    descripcion_proyecto = models.CharField(max_length=5000)
    titular = models.ForeignKey(titular, on_delete=models.CASCADE)
    representante_legal = models.ForeignKey(representanteLegal, on_delete=models.CASCADE)

