
# Institute_Management
A comprehensive Python-based application for managing academic institutions, built using the Django framework. This project follows the MVT architecture, emphasizes modularity, and integrates exception handling for seamless operation.

## Features
- Forgot password feature
- Manage student and faculty records
- Schedule and manage courses
- Generate and view reports
- Role-based user authentication
- Registration page contain validation
- Clean error handling and modular structure

## Project Run Process
Follow these steps to set up and run the project:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/DhruvitSavaliya/Institute_Management.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd Institute_Management
   ```

3. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply database migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (for admin access)**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the application**:
   Open your browser and navigate to:
   ```
   http://127.0.0.1:8000/
   ```

## Admin Panel
Visit:
```
http://127.0.0.1:8000/admin/
```
Log in with your superuser credentials to manage students, faculties, and courses.
- **Username:** dhruvit
- **Email:** dhruvit@gmail.com
- **Password:** dhruvit

## Technologies Used
- **Python** (96.9%)
- **Django** - High-level Python web framework
- **SQLite** (default database)
