# 🧠 Job Portal
![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python)
![Django](https://img.shields.io/badge/Django-5.0-green?logo=django)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## 📋 Overview
**Job Portal** is an web platform that simplifies the process of finding and managing internships for students.  
It connects students, mentors, and organizations through a centralized portal where users can register, upload CVs, view internship listings, and apply directly.  
The system intelligently recommends the best internship matches based on user skills, interests, and qualifications.

---

## 🚀 Key Features
- 🔐 **User Authentication** – Secure sign-up/login system.  
- 📄 **CV Uploads** – Users can upload resumes and manage profiles.  
- 💼 **Internship Listings** – Post, view, and manage internship opportunities.  
- 🎯 **AI-Based Recommendations** – Suggests internships that match a candidate’s profile.  
- 🧾 **Application Tracking** – Monitor internship applications easily.  
- 🖥️ **Admin Dashboard** – Manage users, jobs, and uploaded files.  
- 🗃️ **Media Management** – Supports storage for images, resumes, and videos.

---

## 🏗️ Project Structure
```
teamwork/
│
├── manage.py                # Django management script
├── db.sqlite3               # Default database
├── package.json             # Node dependencies (if any frontend assets)
│
├── myapp/                   # Main Django app
│   ├── admin.py             # Admin panel setup
│   ├── apps.py              # App configuration
│   ├── forms.py             # Django forms
│   ├── models.py            # Database models
│   ├── urls.py              # URL routing
│   ├── views.py             # Business logic
│   ├── utils.py             # Helper functions
│   ├── templates/           # HTML templates
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── job-detail.html
│   │   ├── edit_profile.html
│   │   └── about.html
│   └── migrations/          # Database migrations
│
└── media/                   # Uploaded files (CVs, images, videos)
    ├── cv_uploads/
    └── cvs/
```

---

## ⚙️ Installation & Setup

### 🧩 1. Clone the Repository
```bash
git clone https://github.com/yourusername/teamwork.git
cd teamwork
```

### 🧱 2. Create a Virtual Environment
```bash
python -m venv venv
# Activate:
venv\Scripts\activate      # On Windows
source venv/bin/activate   # On macOS/Linux
```

### 📦 3. Install Dependencies
If you already have a `requirements.txt` file:
```bash
pip install -r requirements.txt
```

If not, install manually:
```bash
pip install django pillow
```

Then create your own:
```bash
pip freeze > requirements.txt
```

### 🗃️ 4. Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 👑 5. Create a Superuser
```bash
python manage.py createsuperuser
```

### 🧠 6. Run the Development Server
```bash
python manage.py runserver
```
Now open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser 🚀

---

## 🧰 Environment Variables (Optional)
Create a `.env` file in the project root for secret keys or environment configs:
```
SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

You can load it using the `python-dotenv` package.

---

## 📁 Media Uploads
All uploaded files (CVs, images, videos) are stored under:
```
media/
  ├── cv_uploads/
  ├── cvs/
  └── other_uploads/
```

Make sure this folder has write permissions:
```bash
mkdir media
```

---

## 🧠 Tech Stack
| Category | Technology |
|-----------|-------------|
| **Backend** | Django (Python) |
| **Frontend** | HTML, CSS (optionally Bootstrap/React) |
| **Database** | SQLite (default) / MySQL / PostgreSQL |
| **Authentication** | Django built-in auth system |
| **Media Handling** | Django `FileField` / `ImageField` |
| **Version Control** | Git & GitHub |

---

## 🧩 API / Future Enhancements
- ✅ Integrate **Django REST Framework** for API access  
- 🧠 Implement **Machine Learning**-based recommendations  
- 📊 Add analytics dashboard for internship insights  
- 📧 Email notification system for application updates  
- 🌐 Deploy on **Render / Railway / Vercel**

---

## 📜 License
This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 👥 Contributors
| Name | Role |
|------|------|
| **Pal Surani & Om Trivedi** | Developer |


---

## 🌟 Acknowledgments
Special thanks to:
- **LJ University** for project support  
- **Smart India Hackathon (SIH)** initiative  
- All mentors and contributors who guided the development  

---

## 💡 How to Contribute
1. Fork this repository  
2. Create a new branch  
3. Commit your changes  
4. Push and create a pull request  

We welcome ideas and improvements 🎉

---

> *“Empowering students through intelligent internship matching.”*  
> Built with ❤️ using **Python & Django**
