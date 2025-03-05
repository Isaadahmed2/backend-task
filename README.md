# 🚀 Django Project Management API

Welcome to the **Django Project Management API**, a backend application built with **Django** and **Django REST Framework (DRF)**. This API allows users to manage projects, assign roles, and add comments while enforcing **Role-Based Access Control (RBAC)**. It also includes an interactive **Swagger UI** for testing endpoints and a **Django admin panel** for managing data.

## 📋 Overview
This project is designed to help users:

- ✅ Register, log in, and authenticate.
- ✅ Create, read, update, and delete projects.
- ✅ Assign roles (**Owner**, **Editor**, **Reader**) to users within projects.
- ✅ Add comments to projects (**Owner** and **Editor** only).
- ✅ Use the **Django admin panel** for managing database models.
- ✅ Test API endpoints interactively using **Swagger** or **Redoc**.

> **Note:** I am still learning Django Rest Framework, so this implementation might not be perfect. However, it fulfills all the core requirements of the assignment, and I’m open to feedback for improvement.

## 🔧 Tech Stack
- **Backend:** Django, Django REST Framework (DRF)
- **Database:** SQLite (default Django database)
- **Authentication:** Django's built-in authentication system
- **API Documentation:** Swagger, Redoc
- **Testing:** Django TestCase
- **Admin Panel:** Django Admin

## 🌟 Features
### 1. User Authentication
- Users can **register**, **log in**, and **log out**.
- Authenticated users receive a **token** for API requests.

### 2. Project Management
- Authenticated users can **create**, **view**, **update**, and **delete** projects.
- Role-based access control ensures only authorized users can perform specific actions:
  - **Owner:** Full CRUD + manage roles.
  - **Editor:** Edit project details and add comments.
  - **Reader:** View-only access.
  - **No Role:** No access.

### 3. Comment Functionality
- **Owners** and **Editors** can add comments to projects.

### 4. Interactive API Documentation
- Use **Swagger** (`/swagger/`) or **Redoc** (`/redoc/`) to test API endpoints interactively.

### 5. Admin Panel
- Manage users, projects, roles, and comments via the **Django admin interface**.

## 🚀 Setup Instructions
Follow these steps to set up and run the project locally:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Isaadahmed2/backend-task
cd backend-task
```

### 2️⃣ Install Dependencies
Ensure you have **Python 3.8+** installed. Then, install dependencies using pip:
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up the Database
Run migrations to set up the SQLite database:
```bash
python manage.py migrate
```

### 4️⃣ Create a Superuser
Create an admin account to access the **Django admin panel**:
```bash
python manage.py createsuperuser
```

### 5️⃣ Start the Development Server
Start the server:
```bash
python manage.py runserver
```
Access the following URLs in your browser:
- **API Endpoints:** http://127.0.0.1:8000/api/
- **Admin Panel:** http://127.0.0.1:8000/admin/
- **Swagger UI:** http://127.0.0.1:8000/swagger/
- **Redoc:** http://127.0.0.1:8000/redoc/

## 📡 API Endpoints

For detailed API endpoints and their descriptions, please refer to the **Redoc** documentation. You will find the complete API structure and information at:

👉 [Redoc API Documentation](http://127.0.0.1:8000/redoc/)

## 🧪 Running Tests
Run the unit tests to ensure everything works as expected:
```bash
python manage.py test
```

## 🎯 Assumptions and Design Decisions
- Used **SQLite** as the default database for simplicity.
- Implemented **role-based access control (RBAC)** using custom permissions.
- Integrated **Swagger** and **Redoc** for interactive API documentation.
- Used Django's built-in authentication system for user management.
- Included basic error handling and validation using DRF serializers.

## 🌱 Areas for Improvement
- 🔄 Improve exception handling and error responses.
- 📊 Optimize database queries for better performance.
- 📝 Enhance API responses with more detailed metadata.
- 🔒 Add additional security measures (e.g., rate limiting, input sanitization).
- 📈 Implement logging for monitoring and debugging.

## 📜 License
This project is licensed under the **MIT License**.

## 🙏 Acknowledgments
Thank you for reviewing my work! I’m still learning **Django Rest Framework**, and this project has been a great opportunity to refresh my knowledge. I’m excited to continue improving and building more robust applications in the future.

If you have any questions or feedback, feel free to reach out! 😊

