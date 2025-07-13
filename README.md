 📝 Collab Editor – Real-Time Collaborative Document Editing Platform

A real-time web-based document collaboration platform that allows multiple users to edit and version control text documents simultaneously, with user authentication, document history, and WebSocket-based live updates.

---

## 📌 Project Description

**Collab Editor** is built using Django + Channels + WebSockets for real-time document editing. The project supports:

- Multi-user login/register with session handling.
- Real-time document updates using WebSocket (via Django Channels).
- Version history management of edited documents.
- Adding/removing collaborators for shared editing.

---

## 🛠️ Tech Stack Used

| Layer         | Technology                                                                 |
|---------------|------------------------------------------------------------------------------|
| 💻 Frontend    | HTML5, CSS3, JavaScript (Vanilla JS)                                        |
| 🧠 Backend     | Django 5.2, Django Channels, ASGI, Daphne                                   |
| 🔌 Realtime    | WebSocket (via Channels and Daphne)                                         |
| 💾 Database    | MySQL 8                                                                    |
| 🌐 Deployment  | AWS EC2 (Ubuntu), Gunicorn/Daphne (for ASGI), Nginx (planned)              |
| 🔒 Auth        | Django Built-in Authentication                                              |
| 🔃 Versioning  | Git, GitHub                                                                |
| ⚙️ Other Tools | systemd (optional), supervisor (optional), tmux (optional)                  |

---

## 🚀 Features

- 👤 **User Registration & Login** (Django Auth)
- 📄 **Create / View / Edit / Delete Documents**
- 🤝 **Real-time Collaborative Editing** (via WebSocket)
- 📜 **Version History** (each edit saved with timestamp)
- 👥 **Add/Remove Collaborators**
- 🔐 **Role-based document access**
- 📬 **Redirects & Auth checks for secured routes**

---

## 🧱 Project Architecture

```plaintext
collab_editor/
├── editor/
│   ├── templates/editor/
│   ├── static/
│   ├── views/
│   │   ├── auth_view.py
│   │   └── document_views.py
│   ├── routing.py       ← WebSocket URLs
│   ├── consumers.py     ← WebSocket logic
│   ├── models.py
│   ├── forms.py
│   └── urls.py
├── collab_editor/
│   ├── asgi.py          ← ASGI app for Daphne/WebSocket
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requirements.txt
⚙️ Local Setup
✅ Prerequisites
Python 3.10+

MySQL 8

Git

Virtualenv (optional but recommended)

🚀 Steps
bash
Copy
Edit
# 1. Clone the repo
git clone https://github.com/yourusername/collab_editor.git
cd collab_editor

# 2. Set up virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install requirements
pip install -r requirements.txt

# 4. Configure DB in collab_editor/settings.py
#    (Use MySQL username, password, and DB name)

# 5. Run migrations
python manage.py migrate

# 6. Run development server
python manage.py runserver
🌐 Deployment on AWS EC2 (Ubuntu)
✅ Setup Steps
SSH into your EC2 instance

Install MySQL, Python, Git

Clone your repo

Set up virtualenv and install dependencies

Configure Django settings + DB

Run app using Daphne:

bash
Copy
Edit
DJANGO_SETTINGS_MODULE=collab_editor.settings daphne -b 0.0.0.0 -p 8000 collab_editor.asgi:application
Open http://<EC2-IP>:8000/ in browser

Ensure port 8000 is open in EC2 security group

🧪 Testing & Debugging
🧪 python manage.py test for basic Django tests.

🕵️ Logs are printed to console.

⚠️ WebSocket issues? Check routing and ASGI config.

🧑‍💻 Developer Notes
ASGI is used instead of WSGI to enable WebSockets.

daphne is used as the ASGI server.

Django Channels handles WebSocket connections.

Security best practices (HTTPS, environment variables, production WSGI) are pending and planned.

Future plan: Add file uploads, markdown support, and rich text formatting.

🔐 Security Checklist
 Use Django Auth system

 Secure MySQL user with limited privileges

 Sanitize document inputs

 Move SECRET_KEY and DB credentials to .env

 Add CSRF protection on all forms

📦 Dependencies
See requirements.txt, but key packages:

ini
Copy
Edit
Django==5.2.4
channels==4.1.0
daphne==4.1.0
mysqlclient==2.2.4
📄 License
MIT License — update this file if needed

🙋‍♂️ Maintainer
Kaushal Kolhe
Email: kolhekaushal2003@gmail.com
LinkedIn: linkedin.com/in/kaushal-kolhe-783587229

