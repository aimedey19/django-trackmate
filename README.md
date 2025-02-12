
# django-trackmate

**django-trackmate** is a lightweight and customizable Django package for tracking API requests, login/logout activities, and user-defined actions within your application. This package is designed to simplify activity tracking and help you gain actionable insights into user behavior.

---

## 🚀 Features

- **Request Logging**: Automatically log incoming API requests with detailed metadata.
- **Login/Logout Tracking**: Monitor user authentication events seamlessly.
- **Custom Action Logs**: Track user actions across your application.
- **Django Admin Integration**: View, filter, and manage activity logs in the admin panel.
- **GenericForeignKey Support**: Log actions related to various models effortlessly.
- **Highly Configurable**: Exclude paths, customize log details, and more.

---

## 📦 Installation

1. Using pip:

   ```bash
   pip install django-trackmate
   ```
   
   or using uv:

   ```bash
   uv add django-trackmate
   ```

2. Add `trackmate` to your `INSTALLED_APPS` in `settings.py`:

   ```python
   INSTALLED_APPS = [
       ...
       'django_trackmate',
   ]
   ```

3. Run migrations to set up the necessary database tables:

   ```bash
   python manage.py makemigrations django_trackmate
   python manage.py migrate
   ```

---

## 🛠 Usage

### Logging Custom Actions
Use the `tracker` decorator to log custom actions:

```python
from django_trackmate import tracker

@tracker()
def my_api_view(request):
    ...
```

### Extending Functionality
Directly create activity logs using the `ActivityLog` model:

```python
from django_trackmate.models import ActivityLog

    ActivityLog.objects.create(
        actor=None,
        action_type=LOGIN_FAILED,
        action_time=datetime.now(),
        remarks=message
    )
```

### Parameters
- `content_object`: An instance of a Django model to link to the activity log.
- `actor`: The user who performed the action.
- `action_type`: The type of action being logged. Choices: "Create", "Read", "Update", "Delete", "Login", "Logout", "Login Failed".
- `action_time`: The timestamp of the action.
- `remarks`: Additional details about the action.
- `ip_address`: The IP address of the user's request.
- `status`: The status of the action. Choices: "Success", "Failed".
- `status_code`: The HTTP status code associated with the action.
- `response`: The response data associated with the action.
- `data`: The request data associated with the action.

---

## 📊 Viewing Logs

- View logs in the Django Admin under the **Activity Logs** section.
- Use filters to sort by user, action type, timestamp, or related object.

---

## 🧪 Running Tests

Run the test suite to ensure everything is functioning correctly:

```bash
python manage.py test trackmate
```

---

## 💡 Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description of the changes.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## 📧 Support

If you encounter any issues or have questions, feel free to open an issue on GitHub or email us at **aime.degbey@kodesio.com**.

---

## 🏗 Built With

- **Django**: The web framework for perfectionists with deadlines.
- **Python**: Simplicity and flexibility for building scalable software.