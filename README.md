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


