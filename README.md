# 📝 Collab Editor – Real-Time Collaborative Document Editing Platform

![Django](https://img.shields.io/badge/Django-5.2-green?style=flat-square&logo=django)
![WebSocket](https://img.shields.io/badge/WebSocket-Enabled-blue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)
![MySQL](https://img.shields.io/badge/MySQL-8.0-blue?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.10+-yellow?style=flat-square)

> A real-time collaborative document editor built with Django, Channels, and WebSocket. Enables live editing, version control, and role-based access for multiple users on shared documents.

---

## 📌 Project Description

**Collab Editor** is a full-stack web application that empowers teams or individuals to create, edit, and collaborate on documents in real time. It features:

- 🧑‍💻 Multi-user registration and login
- 🔄 Real-time editing using Django Channels & WebSockets
- 📜 Document versioning with timestamps
- 🤝 Collaborator management with access control

---

## 🛠️ Tech Stack

| Layer          | Technologies                                                                       |
|----------------|------------------------------------------------------------------------------------|
| 💻 Frontend     | HTML5, CSS3, JavaScript (Vanilla)                                                  |
| 🧠 Backend      | Django 5.2, Django Channels, ASGI, Daphne                                           |
| 🔌 Realtime     | WebSockets via Django Channels + Daphne                                             |
| 💾 Database     | MySQL 8                                                                            |
| ☁ Deployment    | AWS EC2 (Ubuntu), Gunicorn/Daphne (ASGI), Nginx (planned)                          |
| 🔐 Auth         | Django Built-in Authentication                                                     |
| ⚙ Dev Tools     | Git, GitHub, systemd/supervisor (optional), tmux (optional)                        |

---

## 🚀 Key Features

- 👤 **User Authentication** – Register/login using Django's built-in auth system
- 📄 **CRUD Documents** – Create, Read, Update, Delete text documents
- 🌐 **Live Collaboration** – Real-time sync using WebSocket
- 🧾 **Version History** – Track who edited what and when
- 👥 **Collaboration** – Add/remove collaborators to shared documents
- 🛡 **Role-Based Access** – Access control for owners, editors, viewers
- 🔐 **Secure Routes** – Access only allowed to authenticated users

---

## 🧱 Project Architecture

```plaintext
collab_editor/
├── editor/
│   ├── templates/editor/        # HTML Templates
│   ├── static/                  # CSS & JS files
│   ├── views/
│   │   ├── auth_view.py         # Login/Register logic
│   │   └── document_views.py    # Document CRUD
│   ├── routing.py               # WebSocket URLs
│   ├── consumers.py             # WebSocket logic
│   ├── models.py                # Database models
│   ├── forms.py
│   └── urls.py
├── collab_editor/
│   ├── asgi.py                  # ASGI entry point for WebSocket
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requirements.txt

```
## ⚙️ Local Development Setup
- ✅ Prerequisites
- Python 3.10+
- MySQL 8
- Git
- Virtualenv (recommended)

## 💻 Installation Steps
- bash
- Copy
- Edit
# 1. Clone the repository
git clone https://github.com/yourusername/collab_editor.git
cd collab_editor

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install required packages
pip install -r requirements.txt

# 4. Configure MySQL in collab_editor/settings.py

# 5. Apply database migrations
python manage.py migrate

# 6. Run the development server
python manage.py runserver
☁️ Deployment on AWS EC2 (Ubuntu)
✅ EC2 Setup
bash
Copy
Edit
# SSH into EC2
ssh ubuntu@your-ec2-ip

# Install Python, MySQL, and Git
sudo apt update
sudo apt install python3 python3-pip python3-venv mysql-server git

# Clone the repository
git clone https://github.com/yourusername/collab_editor.git
cd collab_editor

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure database settings in settings.py

# Run migrations
python manage.py migrate

# Start the ASGI server using Daphne
DJANGO_SETTINGS_MODULE=collab_editor.settings daphne -b 0.0.0.0 -p 8000 collab_editor.asgi:application
✅ Make sure port 8000 is open in your EC2 security group.


## 🔐 Security Checklist
- ✅ Use Django's built-in authentication system
- ✅ Move SECRET_KEY and DB credentials to .env file
- ✅ Use a MySQL user with limited privileges
- ✅ Sanitize document inputs to prevent XSS/SQLi
- ✅ Add CSRF protection to all forms

## 🧪 Future Enhancements
- 📁 File uploads
- ✍️ Markdown & Rich Text Editor (e.g., Quill.js, TinyMCE)
- 💬 In-document chat system
- 🌍 Multilingual support & grammar suggestions
- 🔒 JWT authentication for API endpoints


## 📦 Key Dependencies
ini
Copy
Edit
Django==5.2.4
channels==4.1.0
daphne==4.1.0
mysqlclient==2.2.4
(Full list available in requirements.txt)


