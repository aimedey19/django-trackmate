# 🎯 django-trackmate

**django-trackmate** is a lightweight and customizable Django package for tracking API requests, login/logout activities, and user-defined actions within your application. This package simplifies activity tracking and provides actionable insights into user behavior.

---

## 🚀 Features

✔ **Request Logging** – Automatically log incoming API requests with detailed metadata.  
✔ **Login/Logout Tracking** – Monitor user authentication events seamlessly.  
✔ **Custom Action Logs** – Track user actions across your application.  
✔ **Django Admin Integration** – View, filter, and manage activity logs in the admin panel.  
✔ **GenericForeignKey Support** – Log actions related to various models effortlessly.  
✔ **Highly Configurable** – Exclude paths, customize log details, and more.  

---

## 📦 Installation

### 1️⃣ Install the package
Using pip:

```bash
pip install django-trackmate
```

or using `uv`:

```bash
uv add django-trackmate
```

### 2️⃣ Add to `INSTALLED_APPS`
Modify your `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'django_trackmate',
]
```

### 3️⃣ Run Migrations
Set up the necessary database tables:

```bash
python manage.py makemigrations django_trackmate
python manage.py migrate
```

---

## 🛠 Usage

### 📝 Logging Custom Actions

Use the `tracker` decorator to log custom actions:

```python
from django_trackmate import tracker

@tracker()
def my_api_view(request):
    ...
```

### 🛡️ Enable Middleware

Add `RequestTrackerMiddleware` to `MIDDLEWARE`:

```python
MIDDLEWARE = [
    ...
    'django_trackmate.middleware.RequestTrackerMiddleware',
]
```

---

## ⚙️ Configuration

Customize logging behavior in `settings.py`:

```python
TRACKMATE_EXCLUDED_PATH = ["/admin/", "/docs/"]  # Paths to exclude from logging
TRACKMATE_LOG_LOGIN_ACTIVITIES = True  # Enable login activity logging (default: True)
```

---

## 📂 Extending Functionality

You can manually create activity logs using the `ActivityLog` model:

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

### 🔍 Available Parameters

| Parameter       | Description |
|----------------|-------------|
| `content_object` | Django model instance linked to the log |
| `actor` | User performing the action |
| `action_type` | Action type (`Create`, `Read`, `Update`, `Delete`, `Login`, `Logout`, `Login Failed`) |
| `action_time` | Timestamp of the action |
| `remarks` | Additional details |
| `ip_address` | IP address of the request |
| `status` | Status (`Success`, `Failed`) |
| `status_code` | HTTP status code |
| `response` | Response data |
| `data` | Request data |

---

## 📊 Viewing Logs

- View logs in **Django Admin** under the **Activity Logs** section.
- Use filters to sort by user, action type, timestamp, or related objects.

### 🎨 Enhancing UI with `django-unfold`

1️⃣ Install `django-unfold`:

```bash
pip install django-unfold
```

2️⃣ Add `unfold` to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'unfold',
    'unfold.contrib.filters',
]
```

3️⃣ Customize the admin panel (`admin.py`):

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

## 🧪 Running Tests (Coming Soon) 🚧

Run tests to ensure everything is working:

```bash
python manage.py test trackmate
```

---

## 💡 Contributing

Contributions are welcome! To contribute:

1️⃣ Fork the repository.  
2️⃣ Create a new branch for your feature or bugfix.  
3️⃣ Submit a pull request with a detailed description.  

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 📧 Support

If you encounter issues or have questions, feel free to:  
📬 Open an issue on **GitHub**  
📩 Email us at **aime.degbey@kodesio.com**

---

## 🏗 Built With

- **Django** – The web framework for perfectionists with deadlines.  
- **Python** – Simplicity and flexibility for scalable software.  
