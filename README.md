# Product Hub - MVP

## 🎯 Project Purpose

A Product Review and Inventory Management system built with Django. This application allows administrators to manage a product catalog while providing a platform for users to read and leave reviews. It is designed to demonstrate a full-stack CRUD application with secure user authentication and responsive design.

## 🚀 Agile Methodology

This project was developed using Agile principles to ensure a structured and iterative development process.

- **GitHub Projects:** Used as a Kanban board to track User Stories and MoSCoW prioritization.
- **User Stories:** Each feature was defined by a User Story with clear Acceptance Criteria and Tasks.
- **Commit History:** Regular, meaningful commits demonstrate the incremental build of the application.

*Link to GitHub Project Board: [INSERT YOUR PROJECT LINK HERE]*

## 🛠️ Technologies Used

- **Language:** Python 3.12
- **Framework:** Django 6.0
- **Frontend:** HTML5, CSS3, Bootstrap 5.3 (via CDN)
- **Database:** SQLite3 (Development), PostgreSQL (Production via Heroku)
- **Deployment:** Heroku
- **Security:** `env.py` used for environment variables; `SECRET_KEY` and `DEBUG` are hidden from version control.

## 🔒 Security Features

- **Environment Variables:** Sensitive data is stored in a local `env.py` file which is excluded from GitHub via `.gitignore`.
- **User Authentication:** Secure login, logout, and registration functionality using Django’s built-in authentication system and custom views.
- **CSRF Protection:** All forms utilize `{% csrf_token %}` to prevent Cross-Site Request Forgery.
- **Debug Mode:** Configured to automatically switch off in production to prevent data leaks.

## 🏗️ Database Schema

### Product Model

- `name`: CharField (200) - The name of the product.
- `description`: TextField - Detailed information about the product.
- `price`: DecimalField - The cost of the product.
- `created_at`: DateTimeField - Automatically set when the product is created.

### Review Model

- `product`: ForeignKey (Product) - Links the review to a specific product.
- `user`: ForeignKey (User) - Links the review to the user who wrote it.
- `content`: TextField - The text of the review.
- `rating`: IntegerField - A rating from 1 to 5.
- `created_at`: DateTimeField - Automatically set when the review is posted.

---

## ✅ Current Implementation Status

- [x]  Django project **`product_hub`** created.
- [x]  Django app **`catalog`** created and added to `INSTALLED_APPS`.
- [x]  Local environment variables configured via `env.py`.
- [x]  **Product Model** implemented, migrated, and registered with Admin.
- [x]  **Responsive Frontend** implemented using Bootstrap 5.
- [x]  **Template Inheritance** used with `base.html` and `product_list.html`.
- [x]  **User Authentication** (Login/Logout/Registration) fully functional.
- [x]  **Review Model** implemented with Foreign Key relationships.
- [x]  **Product Detail View** showing specific product info and associated reviews.
- [x]  **Frontend CRUD**: Logged-in users can create reviews via a frontend form.
- [ ]  Heroku deployment with PostgreSQL.
- [ ]  Manual testing documentation.

---

## 📂 Project Structure (Current)

```
product-hub/
├─ manage.py
├─ env.py
├─ .gitignore
├─ requirements.txt
├─ README.md
├─ db.sqlite3
├─ product_hub/
│  ├─ settings.py
│  └─ urls.py
├─ catalog/
│  ├─ admin.py
│  ├─ forms.py
│  ├─ models.py
│  ├─ urls.py
│  └─ views.py
└─ templates/
   ├─ catalog/
   │  ├─ base.html
   │  ├─ product_list.html
   │  └─ product_detail.html
   └─ registration/
      ├─ login.html
      └─ register.html

```

## 💻 Running the Project Locally

1. **Clone the repository**
    
    ```
    bashCopy
    git clone <your-repo-url>
    cd product-hub
    
    ```
    
2. **Create and activate a virtual environment**
    
    ```
    bashCopy
    python -m venv .venv
    .venv\Scripts\activate
    
    ```
    
3. **Install dependencies**
    
    ```
    bashCopy
    pip install -r requirements.txt
    
    ```
    
4. **Create `env.py`**
In the project root, create `env.py` and add:
    
    ```
    pythonCopy
    import os
    os.environ.setdefault("SECRET_KEY", "your-secret-key-here")
    os.environ.setdefault("DEBUG", "True")
    
    ```
    
5. **Apply migrations & Run**
    
    ```
    bashCopy
    python manage.py migrate
    python manage.py runserver
    
    ```
    
---

## 🧪 Testing

### Manual Testing

- **Navigation:** Verified that "Home", "Admin", "Login", and "Register" links work correctly.
- **Authentication:** Confirmed that only logged-in users can see the "Admin" link and the "Leave a Review" form.
- **CRUD Functionality:** Verified that users can register, log in, and successfully post a review that appears immediately on the product page.
- **Responsiveness:** Tested on various screen sizes using Chrome DevTools to ensure the Bootstrap grid and cards adjust correctly.

---

## 🚢 Deployment (Planned)

The application will be deployed to **Heroku** using the GitHub integration method. Static files will be served via **WhiteNoise**.

---

## 🤖 AI Usage

This project used AI for:

- Project planning and MVP scoping.
- Guidance on Django setup, model relationships, and form handling.
- Troubleshooting "TemplateDoesNotExist" and "ImportError" issues.
- Suggestions for README structure and Bootstrap styling.
