from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
class Laboratorio(models.Model):
    nombre = models.CharField(max_length=100) 
    ciudad = models.CharField(default='Desconocida',max_length=100)
    pais = models.CharField(default='Desconocido',max_length=100)
    class Meta:
        db_table = 'Laboratorio'

    def __str__(self):
        return self.nombre
    
class DirectorGeneral(models.Model):
    nombre = models.CharField( max_length=100)
    laboratorio = models.OneToOneField(Laboratorio,on_delete=models.CASCADE)
    especialidad = models.CharField(default='Sin especificar' ,max_length=100)

    class Meta:
        db_table = 'Director General'

    def __str__(self):
        return self.nombre

def date_validator(value):
    if value.year <= 2014:
        raise ValidationError('La fecha debe ser 2015 o mayor')

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    fecha_fabricacion = models.DateField(validators=[date_validator]) 
    precio_costo = models.DecimalField(max_digits=12,decimal_places=2)
    precio_venta = models.DecimalField(max_digits=12,decimal_places=2)

    class Meta:
        db_table = 'Productos'

    def f_fabricacion_y(self):
        return self.f_fabricacion.year if self.f_fabricacion else None

    def __str__(self):
        return self.nombre