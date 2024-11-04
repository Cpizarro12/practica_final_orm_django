from django.urls import path
from .views import mostrar_lab, insertar_lab,editar_lab,actualizar_lab,eliminar_lab,InicioPageView,AcercaPageView

urlpatterns = [
    path('mostrar/', mostrar_lab, name='mostrar_lab'),
    path('insertar/', insertar_lab, name='insertar_lab'),
    path('editar/<int:pk>', editar_lab, name='editar_lab'),
    path('editar/actualizarlab/<int:id>', actualizar_lab, name='actualizar_lab'),
    path('eliminar/<int:pk>', eliminar_lab, name='eliminar_lab'),
    path("inicio/", InicioPageView.as_view(), name="inicio"),
    path("acerca-de/", AcercaPageView.as_view(), name="acerca-de"),
]