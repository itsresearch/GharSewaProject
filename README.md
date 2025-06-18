
# 🏠 GharSewa - Home Service Booking System

**GharSewa** is an online home service booking platform built using **Python Django**. It connects users with verified service providers (e.g., plumbers, electricians, painters, etc.) through a clean, user-friendly interface. The platform supports user and employee registration, Google Sign-In, real-time booking, and an admin dashboard.

---

## 🚀 Features

- 🔐 User Authentication (Email/Password & Google Login)
- 🧑‍💼 Service Provider Registration
- 🛠️ Browse & Book Home Services
- 📅 Schedule Appointments
- ⭐ User Feedback/Review System
- 📊 Custom Admin Dashboard
- 📁 All user & service data stored in a secure database

---

## 🛠️ Tech Stack

| Technology     | Use Case                       |
|----------------|--------------------------------|
| Django         | Backend Framework              |
| SQLite         | Default Database               |
| HTML/CSS       | Frontend Layout                |
| JavaScript     | Interactions & Form Handling   |
| Bootstrap      | Responsive Design              |
| Google OAuth   | Social Authentication          |

---

## 🔧 Installation

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/gharsewa.git
cd gharsewa
```

2. **Create & Activate Virtual Environment**

```bash
python -m venv env
source env/bin/activate      # On Windows: env\Scripts\activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure Google Login (Optional)**  
   - Add your credentials in `settings.py` under `SOCIAL_AUTH_GOOGLE_*`
   - Create OAuth credentials at: https://console.developers.google.com

5. **Apply Migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Create Superuser**

```bash
python manage.py createsuperuser
```

7. **Run the Server**

```bash
python manage.py runserver
```

Then go to: [http://localhost:8000](http://localhost:8000)

---

## 🖥️ Admin Panel

- URL: `/admin`
- Access: Login with the superuser created above
- Manage users, services, bookings, and feedback from one place

---

## 📂 Project Structure (Important Files)

```
gharsewa/
├── gharsewa/             # Django Project Folder
│   ├── settings.py       # Project Settings
│   └── urls.py           # URL Routing
├── services/             # App for service logic
├── templates/            # HTML Templates
├── static/               # CSS, JS, Images
├── db.sqlite3            # Default database
└── manage.py
```

---

## 📌 Future Enhancements

- Email Notifications
- Payment Integration
- Chat between Users and Providers
- Mobile App Version

---

## 🙏 Acknowledgements

Thanks to:
- Django & Python Community
- Bootstrap for front-end styling
- Google OAuth for seamless login

---

## 📬 Contact

**Developer:** Research Devkota  
📧 Email: researchofficial55@gmail.com  
📍 Location: Kathmandu, Nepal
