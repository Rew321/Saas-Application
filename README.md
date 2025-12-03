# Tenants

A multi-tenant SaaS application built with Django.

## Overview

This is a Django-based SaaS platform designed to manage multiple isolated tenants with separate data and configurations.

## Features

- **Multi-tenant Architecture** - Isolate customer data and configurations
- **User Management** - Handle authentication and authorization per tenant
- **Scalable Design** - Built for growth and flexibility
- **API Support** - RESTful endpoints for integration

## Tech Stack

- **Framework**: Django
- **Database**: PostgreSQL (recommended)
- **Authentication**: Django authentication system
- **API**: Django REST Framework (optional)

## Getting Started

### Prerequisites

- Python 3.8+
- pip
- Virtual environment

### Installation

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

```

### Running the Project

1. Create a new tenant by running `python manage.py create_tenant <tenant_name>`.
2. Create a new user by running `python manage.py createsuperuser --email <email> --password <password>`.
3. Run the development server with `python manage.py runserver`.
4. Open a web browser and navigate to `http://localhost:8000/admin/` to access the admin interface.
5. Log in with the created superuser credentials.
6. Create a new tenant user by navigating to `http://localhost:8000/admin/auth/user/add/` and filling in the required information.
7. Log out and log back in with the created tenant user credentials to access the tenant-specific interface.
## Contributing

See CONTRIBUTING.md for guidelines.

## License

MIT License