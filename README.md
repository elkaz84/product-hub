# Product Hub 

## 🎯 Project Purpose

Product Hub is a **Product Review and Inventory Management** system built with Django. This application allows administrators to manage a product catalog while providing a platform for users to read and leave reviews. It demonstrates a full-stack CRUD application with secure user authentication and responsive design.

## 🚀 Agile Methodology

This project was developed using Agile principles to ensure a structured and iterative development process.

- **GitHub Projects:** Used as a Kanban board to track User Stories and MoSCoW prioritization.  
- **User Stories:** Each feature was defined by a User Story with clear Acceptance Criteria and Tasks.  
- **Commit History:** Regular, meaningful commits demonstrate the incremental build of the application.  
- **Link to GitHub Project Board:**    https://dashboard.heroku.com/apps/product-hub-elkaz84

  ## 🎨 Design & Wireframes
Before coding, I created wireframes to plan the layout for both desktop and mobile. This ensured a consistent user experience across all devices.

### Desktop Tablet and Mobile Wireframe
<img width="2385" height="1907" alt="wireframe_detail_balsamiq" src="https://github.com/user-attachments/assets/49d4cce7-c451-4c6c-8db7-e67628fa2000" />
<img width="2385" height="1907" alt="wireframe_admin_balsamiq" src="https://github.com/user-attachments/assets/8af013fb-0bdf-48ef-92f0-258ff2421edf" />
<img width="2385" height="1907" alt="wireframe_login_balsamiq" src="https://github.com/user-attachments/assets/772ed37b-e2a0-4f3b-beb4-0b89284866d7" />
<img width="2385" height="1907" alt="product_hub_balsamiq" src="https://github.com/user-attachments/assets/42515e97-d4a3-414c-8afd-27dce0cdb04d" />

## 🛠️ Technologies Used

- **Language:** Python 3.12  
- **Framework:** Django 6.0  
- **Frontend:** HTML5, CSS3, Bootstrap 5.3 (via CDN)  
- **Database:** SQLite3 (Development), PostgreSQL (Production via Heroku)  
- **Deployment:** Heroku  
- **Security:** Environment variables via `env.py` (excluded from version control)  

## 🔒 Security Features

- **Environment Variables:** Sensitive data stored in local `env.py` file, excluded from GitHub via `.gitignore`.  
- **User Authentication:** Secure login, logout, and registration using Django’s built-in system and custom views.  
- **CSRF Protection:** All forms use `{% csrf_token %}` to prevent Cross-Site Request Forgery.  
- **Debug Mode:** Automatically switches off in production to prevent data leaks.  


## 🏗️ Database Schema

### Product Model

| Field       | Type          | Description                        |
|-------------|---------------|----------------------------------|
| `name`      | CharField(200)| The name of the product.          |
| `description`| TextField    | Detailed information about product.|
| `price`     | DecimalField  | Cost of the product.              |
| `created_at`| DateTimeField | Auto-set on creation.             |

### Review Model

| Field       | Type          | Description                        |
|-------------|---------------|----------------------------------|
| `product`   | ForeignKey    | Links review to a product.        |
| `user`      | ForeignKey    | Links review to the user.         |
| `content`   | TextField     | Text of the review.               |
| `rating`    | IntegerField  | Rating from 1 to 5.               |
| `created_at`| DateTimeField | Auto-set on posting.              |


## ✅ Current Implementation Status

- Django project `product_hub` created.  
- Django app `catalog` created and added to `INSTALLED_APPS`.  
- Local environment variables configured via `env.py`.  
- Product and Review models implemented, migrated, and registered with Admin.  
- Responsive frontend implemented using Bootstrap 5.  
- Template inheritance used with `base.html`, `product_list.html`, and `product_detail.html`.  
- User authentication (login/logout/registration) fully functional.  
- Frontend CRUD: logged-in users can create reviews via forms.  
- Heroku deployment with PostgreSQL and Cloudinary for media.  
- Manual testing documented.  

---

## 📂 Project Structure (Current)product-hub/
├─ manage.py
├─ env.py
├─ .gitignore
├─ requirements.txt
├─ README.md
├─ db.sqlite3
├─ product_hub/
│ ├─ settings.py
│ └─ urls.py
├─ catalog/
│ ├─ admin.py
│ ├─ forms.py
│ ├─ models.py
│ ├─ urls.py
│ └─ views.py
└─ templates/
├─ catalog/
│ ├─ base.html
│ ├─ product_list.html
│ └─ product_detail.html
└─ registration/
├─ login.html
└─ register.html


## 💻 Running the Project Locally

### Clone the repository

```bash
git clone <your-repo-url>
cd product-hub
Create and activate a virtual environment
Windows (PowerShell):
powershell
Copy
python -m venv .venv
.\.venv\Scripts\activate
macOS/Linux:
bash
Copy
python3 -m venv .venv
source .venv/bin/activate
Install dependencies
bash
Copy
pip install -r requirements.txt
Create env.py
In the project root, create env.py and add:

python
Copy
import os
os.environ.setdefault("SECRET_KEY", "your-secret-key-here")
os.environ.setdefault("DEBUG", "True")
Apply migrations & run server
bash
Copy
python manage.py migrate
python manage.py runserver
Open http://127.0.0.1:8000 in your browser.

🧪 Testing
Manual Testing
Feature	Description	Result	Notes / Screenshots
Navigation	"Home", "Admin", "Login", "Register" links work	Pass	TODO: Add screenshot
Authentication	Only logged-in users see "Admin" and review forms	Pass	TODO: Add screenshot
CRUD Functionality	Users can register, login, post reviews	Pass	TODO: Add screenshot
Responsiveness	Tested on various screen sizes (Chrome DevTools)	Pass	TODO: Add screenshot
Automated Testing
bash
Copy
python manage.py test
Paste your test results here

🚢 Deployment (Planned / Completed)
Deployed to Heroku using GitHub integration.
Static files served via WhiteNoise.
Media files hosted on Cloudinary.
PostgreSQL database via Heroku/NeonDB.
📸 Screenshots

<img width="941" height="452" alt="Image" src="https://github.com/user-attachments/assets/f5cc2287-0a87-48ed-953c-10b1abd89cc6" />
<img width="941" height="452" alt="Image" src="https://github.com/user-attachments/assets/dfaff34e-d011-4e2c-81a0-d8bb383b817f" />
<img width="947" height="443" alt="Image" src="https://github.com/user-attachments/assets/e0efa94f-f5ca-4bd8-aaeb-2281b5b8a3df" />

Lighthouse Scores

📈 Responsiveness & Accessibility
Responsive design tested on desktop, tablet, and mobile devices.
Accessibility features include skip links, ARIA labels, keyboard navigation support, and color contrast compliance.
🔍 SEO & Best Practices
Meta tags for title, description, and Open Graph included.
Semantic HTML used for better SEO and accessibility.
Lighthouse audit scores:

<img width="512" height="412" alt="Image" src="https://github.com/user-attachments/assets/07983d5c-5298-49a0-9cd3-d875ccc8cadd" />
<img width="496" height="380" alt="Image" src="https://github.com/user-attachments/assets/cb233d66-0ad7-41a9-bc8c-dd5b0b7f93af" />

🗂️ Agile Evidence
GitHub Project Board link: TODO
User Stories with acceptance criteria documented.
Commit history shows incremental development.
⚙️ Environment Variables
Variable	Description	Example / Notes
SECRET_KEY	Django secret key	Stored in env.py or Heroku
DEBUG	Debug mode (True/False)	True for local, False prod
DATABASE_URL	Postgres connection string	Provided by Heroku/NeonDB
CLOUDINARY_URL	Cloudinary API URL for media storage	cloudinary://...
🛠️ Useful Commands
bash
Copy
# Activate virtual environment (Windows)
.\.venv\Scripts\activate

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver

# Collect static files locally
python manage.py collectstatic --noinput

# Run tests
python manage.py test

# Heroku commands (run in Heroku CLI)
heroku run python manage.py migrate --app <your-app-name>
heroku run python manage.py collectstatic --noinput --app <your-app-name>
🐞 Known Issues & Troubleshooting
Admin panel unstyled after deployment:
Ensure collectstatic ran successfully on Heroku.
Check STATICFILES_DIRS points to existing folder.
Add .gitkeep to empty static/ folder if needed.
Images not showing on live site:
Confirm CLOUDINARY_URL is set in Heroku Config Vars.
Upload images via live admin to store on Cloudinary.
Heroku filesystem is ephemeral; local uploads won’t persist.
🔮 Future Improvements
Add product search and filtering.
User profiles and avatars.
Email notifications for reviews.
Automated CI/CD with tests and linting.
🙏 Credits & Acknowledgements
Code Institute LMS and tutors
Bootstrap, Cloudinary, Heroku
Unsplash and Pexels for free images
ChatGPT for code and documentation assistance
W3Schools and MDN for web development references

Thank you for visiting Product Hub!
Feel free to contribute or raise issues.



