# Site Survey Backend

This project is a FastAPI-based backend for managing site survey data. It provides APIs for various functionalities, including user management, project management, and site-related operations.

## Features
- User management
- Project management
- Role-based access control
- Site location, information, and access management
- Survey visit tracking
- Static file serving (e.g., signup page)
- CORS support for frontend integration

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Wajeeha-Imtiaz-786/SEE-SURVEY-PROJECT.git
   ```

2. Navigate to the project directory:
   ```bash
   cd SEE-SURVEY-PROJECT
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

5. Access the API documentation at:
   - Swagger UI: `http://127.0.0.1:8000/docs`
   - ReDoc: `http://127.0.0.1:8000/redoc`

## Project Structure
```
SE Tool/
├── core/                # Core utilities and configurations
├── crud/                # CRUD operations for database models
├── models/              # Database models
├── routers/             # API route definitions
├── schemas/             # Pydantic schemas for request/response validation
├── static/              # Static files (e.g., HTML, CSS, JS)
├── database.py          # Database connection and setup
├── main.py              # Application entry point
├── requirements.txt     # Python dependencies
```

## API Endpoints

### Health Check
- `GET /`: Verify the API is running.

### Static Pages
- `GET /signup`: Serve the signup page.

### Users
- `GET /users`: List all users.
- `POST /users`: Create a new user.

### Projects
- `GET /projects`: List all projects.
- `POST /projects`: Create a new project.

### Roles
- `GET /roles`: List all roles.
- `POST /roles`: Create a new role.

### Site Location
- `GET /site-location`: List all site locations.
- `POST /site-location`: Add a new site location.

### Survey Visit
- `GET /survey-visit`: List all survey visits.
- `POST /survey-visit`: Add a new survey visit.

### Site Information
- `GET /site-information`: List all site information.
- `POST /site-information`: Add new site information.

### Site Access
- `GET /site-access`: List all site access records.
- `POST /site-access`: Add a new site access record.

## License
This project is licensed under the MIT License.