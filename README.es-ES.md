

# 🎯 django-trackmate

**django-trackmate** es un paquete de Django ligero y personalizable para registrar solicitudes de API, actividades de inicio/cierre de sesión y acciones definidas por el usuario dentro de su aplicación. Este paquete simplifica el seguimiento de actividades y proporciona información accionable sobre el comportamiento del usuario.

---

## 🚀 Características

✔ **Registro de solicitudes** – Registra automáticamente las solicitudes entrantes de la API con metadatos detallados.  
✔ **Seguimiento de inicio/cierre de sesión** – Monitorea sin problemas los eventos de autenticación de usuarios.  
✔ **Registros de acciones personalizadas** – Rastrea las acciones de los usuarios en toda tu aplicación.  
✔ **Integración con Django Admin** – Visualiza, filtra y administra los registros de actividad en el panel de administración.  
✔ **Soporte para GenericForeignKey** – Registra acciones relacionadas con varios modelos sin esfuerzo.  
✔ **Altamente configurable** – Excluye rutas, personaliza los detalles del registro y más.  

---

## 📦 Instalación

### 1️⃣ Instala el paquete
Usando pip:

```bash
pip install django-trackmate
```

o usando `uv`:

```bash
uv add django-trackmate
```

### 2️⃣ Agregar a `INSTALLED_APPS`
Modifica tu `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'django_trackmate',
]
```

### 3️⃣ Ejecutar migraciones
Configura las tablas de base de datos necesarias:

```bash
python manage.py makemigrations django_trackmate
python manage.py migrate
```

---

## 🛠 Uso

### 📝 Registro de acciones personalizadas

Usa el decorador `tracker` para registrar acciones personalizadas:

```python
from django_trackmate import tracker

@tracker()
def my_api_view(request):
    ...
```

### 🛡️ Habilitar Middleware

Agrega `RequestTrackerMiddleware` a `MIDDLEWARE`:

```python
MIDDLEWARE = [
    ...
    'django_trackmate.middleware.RequestTrackerMiddleware',
]
```

---

## ⚙️ Configuración

Personaliza el comportamiento del registro en `settings.py`:

```python
TRACKMATE_EXCLUDED_PATH = ["/admin/", "/docs/"]  # Paths to exclude from logging
TRACKMATE_LOG_LOGIN_ACTIVITIES = True  # Enable login activity logging (default: True)
```

---

## 📂 Ampliar la funcionalidad

Puedes crear manualmente registros de actividad usando el modelo `ActivityLog`:

```python
from django_trackmate.models import ActivityLog
from datetime import datetime

ActivityLog.objects.create(
    actor=None,
    action_type="LOGIN_FAILED",
    action_time=datetime.now(),
    remarks="Invalid credentials"
)
```

### 🔍 Parámetros disponibles

| Parámetro       | Descripción |
|----------------|-------------|
| `content_object` | Instancia de modelo de Django vinculada al registro |
| `actor` | Usuario que realiza la acción |
| `action_type` | Tipo de acción (`Create`, `Read`, `Update`, `Delete`, `Login`, `Logout`, `Login Failed`) |
| `action_time` | Marca de tiempo de la acción |
| `remarks` | Detalles adicionales |
| `ip_address` | Dirección IP de la solicitud |
| `status` | Estado (`Success`, `Failed`) |
| `status_code` | Código de estado HTTP |
| `response` | Datos de la respuesta |
| `data` | Datos de la solicitud |

---

## 📊 Visualización de registros

- Visualiza los registros en **Django Admin** bajo la sección **Activity Logs**.
- Usa filtros para ordenar por usuario, tipo de acción, marca de tiempo u objetos relacionados.

### 🎨 Mejorar la interfaz con `django-unfold`

1️⃣ Instala `django-unfold`:

```bash
pip install django-unfold
```

2️⃣ Agrega `unfold` a `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'unfold',
    'unfold.contrib.filters',
]
```

3️⃣ Personaliza el panel de administración (`admin.py`):

```python
from django.contrib import admin
from django_trackmate.models import ActivityLog
from unfold.admin import ModelAdmin
from unfold.contrib.filters.admin import RangeDateFilter

@admin.register(ActivityLog)
class ActivityLogAdmin(ModelAdmin):
    list_display = ('id', 'actor', 'action_type', 'action_time', 'status_code', 'status', 'remarks')
    list_filter = ("action_type", "status_code", ("action_time", RangeDateFilter))  # Date filter
```

---

## 🧪 Ejecutar pruebas (Próximamente) 🚧

Ejecuta las pruebas para asegurarte de que todo funcione correctamente:

```bash
python manage.py test trackmate
```

---

## 💡 Contribuciones

¡Las contribuciones son bienvenidas! Para contribuir:

1️⃣ Haz un fork del repositorio.  
2️⃣ Crea una nueva rama para tu función o corrección de errores.  
3️⃣ Envía un pull request con una descripción detallada.  

---

## 📄 Licencia

Este proyecto está licenciado bajo la **Licencia MIT**. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

## 📧 Soporte

Si encuentras problemas o tienes preguntas, no dudes en:  
📬 Abrir un issue en **GitHub**  
📩 Envíanos un correo a **aime.degbey@kodesio.com**

---

## 🏗 Construido con

- **Django** – El framework web para perfeccionistas con fechas límite.  
- **Python** – Simplicidad y flexibilidad para software escalable.
