from django.contrib import admin
from django.urls import path
from reto import views

urlpatterns = [
    path('', views.Unidad_Educativa, name="Unidad Educativa"),
    path('Unidad_Educativa/', views.Unidad_Educativa, name="Unidad_Educativa"),
    path('Administrador/', views.Administrador, name="Administrador"),
    path('LOGIN/', views.LOGIN, name="LOGIN"),
    path('Carga_de_documentos/', views.Carga_de_documentos, name="Carga de documentos"),
    path('admin/', admin.site.urls),
]
