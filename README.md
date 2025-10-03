# M6_AE2_ABP - Setup Django en WSL

## ¿Qué es pip?

`pip` es el instalador de paquetes de Python. Permite gestionar librerías desde PyPI
(install, upgrade, uninstall). Buenas prácticas: usarlo siempre dentro de un entorno
virtual para aislar dependencias.

## Archivos clave
- `config/settings.py`: configuración global (INSTALLED_APPS, MIDDLEWARE, TEMPLATES, DATABASES, etc.)
- `config/urls.py`: enrutamiento URL a vistas.
- `config/__init__.py`: inicializa el paquete Python.
- `manage.py`: CLI para comandos de administración (runserver, migrate, createsuperuser).
