# practica_final_orm_django
## Practica de consolidación M7
## Descripcion
- Estado inicial del proyecto

## Tecnologías utilizadas
- VSCode
- Google Chrome
- Python 3.12.4

## Creación del entorno virtual con venv
- nombre del entorno virtual: practica_final_orm_django_venv

## Modelos:
 ### Laboratorio:
- nombre: cadena de caracteres.
### DirectorGeneral:
- nombre: cadena de caracteres.
- laboratorio: Laboratorio.
### Producto:
- nombre: cadena de caracteres.
- laboratorio: Laboratorio.
- f_fabricacion: Tipo fecha que comienza desde el 2015.
- p_costo: decimal con 2 dígitos decimales, y 10 dígitos en la parte entera.
- p_venta: decimal con 2 dígitos decimales, y 10 dígitos en la parte entera.
### Restricciones
- Un laboratorio posee un solo director general.
- Un director general solo puede pertenecer a un laboratorio.
- Un laboratorio fabrica muchos productos para determinado tratamiento médico, y dichos
productos fabricados pertenecen a un sólo laboratorio

## Adecuando sitio administrativo:

- incluyendo los modelos en el sitio administrativo:
```
admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)
```
- Adecuando para que se vea como es solicitado:

```
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'nombre',)
    ordering = ('id',)

class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'nombre',
                    'laboratorio',)
    ordering = ('id',)
    
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'nombre',
                    'laboratorio',
                    'fecha_fabricacion',
                    'precio_costo',
                    'precio_venta',)
    list_select_related = ['laboratorio']

    list_filter = ('nombre',
                'laboratorio',)
    ordering = ('id',)

```
## Consultas a la base de datos a través de la shell
- Se utiliza py manage.py shell para empezar a trabajar en el entorno interactivo.
- Se importan los modelos.

## Obtenga todos los objetos tanto Laboratorio, DirectorGeneral y Productos.
```
>>> laboratorios = Laboratorio.objects.all()
>>> print(laboratorios)
<QuerySet [<Laboratorio: laboratorio1>, <Laboratorio: laboratorio2>, <Laboratorio: laboratorio3>]>
>>> directores_generales = DirectorGeneral.objects.all() 
>>> print(directores_generales) 
<QuerySet [<DirectorGeneral: Director General 1>, <DirectorGeneral: Director General 2>, <DirectorGeneral: Director General 3>]>
>>> productos = Producto.objects.all()  
>>> print(productos) 
<QuerySet [<Producto: Producto1>, <Producto: Producto2>, <Producto: Producto3>]>

```

## Obtenga el laboratorio del Producto cuyo nombre es ‘Producto 1’.
```
>>> producto_1 = Producto.objects.get(nombre='Producto1')  
>>> print(producto_1.laboratorio.nombre)
laboratorio1
```

## Ordene todos los productos por nombre, y que muestre los valores de nombre y laboratorio
```
>>> productos_ordenados = Producto.objects.order_by('nombre')
>>> for producto in productos_ordenados:
...     print(f'Producto: {producto.nombre} Laboratorio: {producto.laboratorio.nombre}')
...
Producto: Producto1 Laboratorio: laboratorio1
Producto: Producto2 Laboratorio: laboratorio2
Producto: Producto3 Laboratorio: laboratorio3

```
## Realice una consulta que imprima por pantalla los laboratorios de todos los productos.
```
>>> for producto in Producto.objects.all():
...     print(f'{producto.nombre} {producto.laboratorio.nombre}') 
...
Producto1 laboratorio1
Producto2 laboratorio2
Producto3 laboratorio3

```
## Modificaciones a los modelos:
- Se agregan nuevos campos, comenzando con laboratorio:
```
    ciudad = models.CharField(default='Desconocida',max_length=100)
    pais = models.CharField(default='Desconocido',max_length=100)
```
- Director general:
```
 especialidad = models.CharField(default='Sin especificar' ,max_length=100)
```
## Aplicación Crud:
- Se crean las vistas, posteriormente los templates y finalmente las urls.

## Pruebas:
