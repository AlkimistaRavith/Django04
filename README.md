# Django04
Django con base de datos

# PASOS: 
## Crear entorno: 
- python -m venv entorno

## Activar entorno:
- source entorno/bin/activate

## Instala Djgango:
- pip install django
- pip install -r requirements.txt

## Levanta proyecto:
- django-admin startproject proyecto .

## Migraciones:
- python manage.py makemigrations
- python manage.py migrate

## Crear super usuario:
- python manage.py createsuperuser

## Para habilitar host:
### En setting.py, bajo ALLOWED_HOSTS = [] (linea 28):
- CSRF_TRUSTED_ORIGINS = [ "https://localhost:8000", ]

## correr servidor:
- python manage.py runserver

## Crear app:
- python manage.py startapp "NOMBRE"

### Agregar app a setting.py del proyecto en linea 36:
- INSTALLED_APPS = [ ... "mi_app", ]

### Crear archivo ulrs.py en app. 
### Crear carpeta templates fuera. 
### Modificar setting.py linea 61 "DIR":
- "DIRS": [BASE_DIR / "templates"],

## En urls.py del proyecto, agregar un archivo de rutas externo: 
### linea 19 (agregar include):
- from django.urls import path, include
### linea 23: 
- path("mi_app/", include("mi_app.urls")),

## Modificar urls.py de la app (mi_app):
- from django.urls import path
- urlpatterns = [ "POR AGREGAR" ]

# ACA COMENZAMOS A CREAR LAS VITAS! 
## Modificar views.py de app agregando función:
- def hola(request): 
-   return render(request, "Hola.html")

## Agregar la ruta en urls.py de la app:
- from django.urls import path 
- from .views import hola
- urlpatterns = [ path("hola/", hola) ]

## Crear un archivo hola.html en carpeta templates

###Modificar html ###Para guardar imagenes en carpeta aparte: agregar en setting.py MEDIA_URL = "/media/" MEDIA_ROOT = BASE_DIR / "media"

###Luego en urls del proyecto agregar: if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)