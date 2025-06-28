# Smart Grace Mark Calculator

A Django-based web application for automating the calculation and management of grace marks. This project is designed to streamline the process for educational institutions, allowing for robust mark entry, computation, and reporting.

## Features

- **User Authentication**: Login system provided via the `login` app.
- **Grace Mark Calculation**: Core logic to automate the calculation of grace marks according to institution-specific rules.
- **Admin Interface**: Standard Django admin panel enabled for superuser management.
- **Media & Static Files**: Organized handling of static assets and uploaded media.
- **Email Notifications**: Configured to use SMTP for notification and reporting.
- **Dockerized Deployment**: Ready-to-deploy with Docker and CI/CD support via Jenkins.

## Project Structure

```
├── Dockerfile
├── Jenkinsfile
├── manage.py
├── db.sqlite3
├── assets/
├── login/
├── media/
├── smart/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── static/
├── templates/
```

- **manage.py**: Django’s command-line utility.
- **smart/**: Main project settings and configuration.
- **login/**: Handles user authentication and related logic.
- **media/** and **static/**: Store uploaded files and static assets.
- **templates/**: HTML templates for UI rendering.

## Setup & Installation

### Prerequisites

- Python 3.x
- Docker (optional, for containerized deployment)
- pip

### Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/varunmedi/smart_garce_mark_calcluator.git
   cd smart_garce_mark_calcluator
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

5. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

6. Access the application at `http://127.0.0.1:8000/`

### Docker Deployment

1. **Build and run the container:**
   ```bash
   docker build -t smart_garce_mark_calcluator .
   docker run -p 8000:8000 smart_garce_mark_calcluator
   ```

### Jenkins CI/CD

- The `Jenkinsfile` provides a pipeline for continuous integration, including:
  - Cloning the repository
  - Installing dependencies (`django`, `pillow`)
  - (Extend as needed for testing and deployment)

## Configuration

Key settings in `smart/settings.py`:
- **Database**: Uses SQLite by default.
- **Static & Media files**:
  - Static: `/static/` (collected in `/assets/`)
  - Media: `/media/` (stored in `/media/`)
- **Email**: SMTP configured for notifications (update credentials in production).
- **Allowed Hosts**: Set to `*` for development; restrict in production.

## URL Routing

Defined in `smart/urls.py`:
- `/` routes to the `login` app (main user interface).
- `/admin/` for Django admin interface.
- Media URLs are served in development.

## Security

- **Debug mode is enabled** by default. **Disable in production!**
- **Secret key** and email credentials are hardcoded – move to environment variables for production.
- **Allowed hosts** is set to `*` – restrict in production.

## Contributing

Contributions, issues, and feature requests are welcome! Please open an issue or submit a pull request.
