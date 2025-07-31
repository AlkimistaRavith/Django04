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

## Modificar html 
### Para guardar imagenes en carpeta aparte: 
- Agregar en setting.py: MEDIA_URL = "/media/" MEDIA_ROOT = BASE_DIR / "media"

## Luego en urls del proyecto agregar:
- if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# ACA COMENZAMOS A CREAR LOGIN DE USUARIOS

## Crear una app aparte (usuario, account, etc)
- Agrergar app a setting.
- Agregar urls de app, a urls del proyecto.

## Agregar en setting del proyecto, línea 71:
- LOGIN_URL = "login"
- LOGIN_REDIRECT_URL = "home"
- LOGOUT_REDIRECT_URL = "login"

## Utilizar las views y formularios de Django, configurando urls.py de la app:
- from django.urls import path
- from .views import registro
- from django.contrib.auth import views as v
- urlpatterns = [
    path("registro/", registro, name="registro"),
    path("login/", v.LoginView.as_view(template_name="usuarios/login.html") , name="login"),
    path("logout/", v.LogoutView.as_view(), name="logout")
    ]

## En views, configurar con el siguient codigo:
### agregar redirect a la importación de shortcuts. Agregar django.contrib.auth.forms para las formularios django, y el formulario de creación de usuario
- from django.shortcuts import render, redirect
- from django.contrib.auth.forms import UserCreationForm
### Definir el metodo de registro, con POST, validando la informacion ingresada y guardando los usuarios correctos.
- def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "usuarios/registro.html", {"form": form})

## Crear templates de login.html y registro.html:
### Ambos deben tener el mismo codigo incluido:
-     <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Registrarme!</button>
    </form>
