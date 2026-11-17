# Census Automation System

A Django web application for structured demographic collection and census administration, developed as a full-stack project.

## Features

- User registration and authentication.
- Demographic forms covering household, employment, education and housing.
- Form validation, record updates, dashboard and real-time data endpoints.
- Django migrations and model/form/view tests.

## Repository map

- `Census_Automation_System/manage.py`: Django entry point.
- `Census_Automation_System/census/`: application models, forms, views, tests and migrations.
- `Census_Automation_System/templates/` and `static/`: frontend resources.
- `Census_Automation_System/Census_Automation_System/`: project configuration.

## Local setup

The source lives on `master`. Clone that branch, enter the inner application folder, and use a fresh local database:

```bash
git clone --branch master https://github.com/takitamim/Census_Automation_System.git
cd Census_Automation_System/Census_Automation_System
```
```powershell
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python manage.py migrate
.venv\Scripts\python manage.py runserver
```

Open http://127.0.0.1:8000. On Linux/macOS, use `.venv/bin/python` in place of `.venv\Scripts\python`.

The dependency file captures a broad development environment and may need platform-specific installation adjustments. Review settings before deployment; local development settings are not a production security configuration. Historical Render/PostgreSQL deployment is described in my résumé.

## Checks

```bash
python manage.py check
python manage.py test census
```

Application behavior and dependency installation were not revalidated during this documentation cleanup.
