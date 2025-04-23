# 🌟 Simple Django Blog

<div align="center">
  
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

</div>

<div align="center">
  <img src="https://github.com/ffiruzi/Simple-Django-Blog/blob/main/screenshot.png" alt="Simple Django Blog Screenshot" width="800px"/>
  <p><em>screenshot of the project</em></p>
</div>

## 📜 Overview

A straightforward, minimal blog platform built with the Django web framework. This project serves as a foundational example demonstrating core Django concepts, including models, the admin site, views, URL routing, templates, static/media file handling, with a touch of modern styling and responsive design.

It includes a robust user authentication system that allows users to create accounts, manage profiles, and author their own blog posts with full CRUD functionality.

It's designed to be easy to understand and extend, making it a great starting point for learning Django or showcasing web development skills.

## ✨ Features

### Core Features
- 📝 Create, view, and manage blog posts and categories
- 👤 Complete user authentication (register, login, logout)
- 👥 User profiles with customizable bio and profile picture
- 🔒 Permission-based access (only authors can edit their own posts)
- 📷 Upload and display images for each blog post
- 🎨 Clean, minimal, and responsive design with a two-column layout
- 📱 Mobile-friendly interface for reading on any device

### User Authentication
- ✅ Register new accounts with email verification
- 🔑 Secure login and session management
- 👤 Personalized user profiles
- 🖼️ Profile picture upload
- 🔗 Custom website URL for each user
- 📝 Bio section for users to describe themselves

### Post Management
- 📝 Create new posts with title, content, category, and image
- ✏️ Edit your own posts
- 🗑️ Delete your own posts
- 👁️ View posts by specific authors
- 🏷️ Categorize posts for better organization

## 🛠️ Technologies Used

- **Backend**: Django (Python Web Framework)
- **Frontend**: HTML, CSS
- **Database**: SQLite (default for Django, included)
- **Image Handling**: Pillow (Python Imaging Library)
- **Authentication**: Django's built-in auth system with custom extensions

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

1. Register a new user account or log in with your superuser credentials
2. Navigate to your profile and fill out your bio and profile picture (optional)
3. Create a new post from the navigation bar or your profile page
4. Assign a category and upload an image (optional)
5. View your published content on the main site or your profile page

## 📁 File Structure Overview

The project follows a standard Django project structure:

```
Simple-Django-Blog/
├── manage.py                # Django's command-line utility
├── simpleblogproject/       # Main project configuration files
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py          # Project settings (database, installed apps, static/media config)
│   ├── urls.py              # Project-level URL patterns (includes blog app urls, media serving)
│   └── wsgi.py
├── blog/                    # Blog application directory
│   ├── migrations/          # Database migration files
│   ├── __init__.py
│   ├── admin.py             # Admin registrations for models
│   ├── apps.py
│   ├── forms.py             # Forms for authentication and post management
│   ├── models.py            # Database models (Post, Category, UserProfile)
│   ├── tests.py             # Placeholder for app tests
│   ├── urls.py              # App-level URL patterns
│   └── views.py             # Logic to handle requests and return responses
├── templates/               # Project-level templates directory
│   └── blog/
│       ├── base.html        # Base template with navigation and common elements
│       ├── post_list.html   # Template for displaying list of posts
│       ├── post_detail.html # Template for displaying a single post
│       ├── register.html    # User registration form
│       ├── login.html       # User login form
│       ├── profile.html     # User profile management
│       ├── author_profile.html  # View another user's profile
│       ├── post_form.html   # Form for creating/editing posts
│       └── post_confirm_delete.html # Confirmation for post deletion
├── static/                  # Project-level static files directory
│   └── css/
│       └── style.css        # Custom CSS for styling
├── media/                   # Directory for user-uploaded media files
│   ├── blog_images/         # Blog post images
│   └── profile_pics/        # User profile pictures
├── venv/                    # Python Virtual Environment
└── requirements.txt         # Project dependencies list
```

## 🚀 Future Enhancements

This project provides a solid starting point. Here are some ideas for future development to enhance its features:

- 💬 Commenting feature for blog posts
- 🔍 Search functionality for finding posts
- 📄 Pagination for the blog list page
- 📝 Rich text editor for post content
- 📊 Analytics dashboard for tracking post views
- 📱 Social media sharing buttons
- 🔔 Notification system for new posts
- 🔑 Social authentication options (Google, Facebook, etc.)
- 📧 Email subscription for blog updates
- 🏷️ Tag system for more granular content organization
- 🧪 Comprehensive test suite

## 📜 License

This project is licensed under the MIT License.

---

<div align="center">
  <p>Made with ❤️ by <a href="https://github.com/ffiruzi">ffiruzi</a></p>
</div>