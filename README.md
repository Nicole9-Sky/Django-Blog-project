# 🌟 Simple Django Blog

<div align="center">
  
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

</div>

<div align="center">
  <img src="https://via.placeholder.com/800x400?text=Simple+Django+Blog" alt="Simple Django Blog Screenshot" width="800px"/>
  <p><em>Replace this placeholder with your actual screenshot</em></p>
</div>

## 📜 Overview

A straightforward, minimal blog platform built with the Django web framework. This project serves as a foundational example demonstrating core Django concepts, including models, the admin site, views, URL routing, templates, and static/media file handling, with a touch of modern styling and responsive design.

It's designed to be easy to understand and extend, making it a great starting point for learning Django or showcasing basic web development skills.

## ✨ Features

- ✅ Create, view, and manage blog posts and categories via the Django admin interface
- 📷 Upload and display images for each blog post
- 🎨 Clean, minimal, and responsive design with a two-column layout for the blog list on wider screens
- 📱 Mobile-friendly interface for reading on any device
- 📄 Basic display of individual post details

## 🛠️ Technologies Used

- **Backend**: Django (Python Web Framework)
- **Frontend**: HTML, CSS
- **Database**: SQLite (default for Django, included)
- **Image Handling**: Pillow (Python Imaging Library)

## 🚀 Setup and Installation

Follow these steps to get the Simple Django Blog Platform running on your local machine after cloning the repository.

### Prerequisites

- Python (3.9 or higher)
- pip (Python package installer)
- git (Version control system)

### Installation Steps

#### 1. Clone the Repository

```bash
git clone https://github.com/ffiruzi/Simple-Django-Blog.git
cd Simple-Django-Blog
```

#### 2. Set up a Virtual Environment

```bash
# Create a virtual environment named 'venv'
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Database Setup

```bash
python manage.py migrate
```

#### 5. Create a Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts in your terminal to set the username, email, and password for your admin account.

#### 6. Run the Development Server

```bash
python manage.py runserver
```

The blog will be accessible in your web browser at http://127.0.0.1:8000/. The administration panel, where you can add and manage content, is located at http://127.0.0.1:8000/admin/.

## 📝 Adding Content

To populate the blog with content:

1. Log in to the Django administration panel (http://127.0.0.1:8000/admin/) using the superuser credentials you created
2. Add categories for your posts
3. Create blog posts, assign categories, and upload images
4. View your published content on the main site

## 📁 File Structure Overview

The project follows a standard Django project structure:

```
Simple-Django-Blog/
├── manage.py           # Django's command-line utility
├── simpleblogproject/  # Main project configuration files
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py     # Project settings (database, installed apps, static/media config)
│   ├── urls.py         # Project-level URL patterns (includes blog app urls, media serving)
│   └── wsgi.py
├── blog/               # Blog application directory
│   ├── migrations/     # Database migration files
│   ├── __init__.py
│   ├── admin.py        # Admin registrations for models
│   ├── apps.py
│   ├── models.py       # Database models (Post, Category with ImageField)
│   ├── tests.py        # Placeholder for app tests
│   ├── urls.py         # App-level URL patterns (post list, post detail)
│   └── views.py        # Logic to handle requests and return responses
├── templates/          # Project-level templates directory (for organization)
│   └── blog/
│       ├── post_list.html  # Template for displaying list of posts (using CSS grid)
│       └── post_detail.html# Template for displaying a single post (styled)
├── static/             # Project-level static files directory
│   └── css/
│       └── style.css   # Custom CSS for styling (minimal & modern, 2-column layout)
├── media/              # Directory for user-uploaded media files
├── venv/               # Python Virtual Environment
└── requirements.txt    # Project dependencies list
```

## 🚀 Future Enhancements

This project provides a solid starting point. Here are some ideas for future development to enhance its features:

- 👥 User registration and authentication system for blog authors
- 💬 Commenting feature for blog posts
- 🏷️ Tagging system for better content organization
- 🔍 Search function for blog posts
- 📄 Pagination for the blog list page
- 📝 Rich text editor for post content in the admin
- 🧪 Writing unit and integration tests
- 🌐 Deployment options (e.g., Heroku, PythonAnywhere, Vercel)

## 📜 License

This project is licensed under the MIT License.

---

<div align="center">
  <p>Made with ❤️ by <a href="https://github.com/ffiruzi">ffiruzi</a></p>
</div>
