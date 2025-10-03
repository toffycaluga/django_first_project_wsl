# Informe M6_AE2_ABP - Instalación y primer proyecto Django (WSL)

## 1. Instalación de Django
- Verifiqué pip: `pip3 --version`.
- Creé entorno virtual: `python3 -m venv .venv` y lo activé con `source .venv/bin/activate`.
- Actualicé pip: `python -m pip install --upgrade pip wheel`.
- Instalé Django: `pip install "Django>=4.2,<6.0"`.
- Verifiqué versión: `python -m django --version`.
- Congelé dependencias: `pip freeze > requirements.txt`.

**Aprendizaje**: pip administra paquetes; es clave aislar dependencias con venv.

## 2. Creación de proyecto
- `django-admin startproject config .`
- Archivos clave:
  - `config/settings.py`: configuración global.
  - `config/urls.py`: rutas.
  - `config/__init__.py`: paquete Python.
  - `manage.py`: comandos administrativos.

**Aprendizaje**: `startproject` genera estructura base y utilidades.

## 3. Servidor y Admin
- Migraciones iniciales: `python manage.py migrate`.
- Servidor: `python manage.py runserver` → `http://localhost:8000`.
- Superusuario: `python manage.py createsuperuser` → `http://localhost:8000/admin`.

**Aprendizaje**: migraciones crean tablas; admin listo sin código extra.

## 4. Configuración de Templates y URLs
- Carpeta `templates/` en raíz y `templates/index.html`.
- `settings.py` → `TEMPLATES['DIRS'] = [BASE_DIR / 'templates']`.
- `urls.py` → `TemplateView` para `/`.

**Aprendizaje**: separar templates a nivel proyecto y enrutar sin crear app.

## 5. Buenas prácticas aplicadas
- Trabajar en WSL dentro de `$HOME` (evitar `/mnt/c`).
- Entorno virtual por proyecto.
- `requirements.txt` para reproducibilidad.
- `.gitignore` para artefactos.
- Commits pequeños, descriptivos y numerados.

## 6. Evidencias (capturas sugeridas)
1) `pip3 --version`
2) `python -m django --version`
3) Estructura de proyecto (árbol)
4) `python manage.py runserver` y página de bienvenida
5) Login del admin
6) Dashboard del admin
7) Página `/` con `index.html`

