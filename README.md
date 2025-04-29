# 🌟 Simple Django Blog

<div align="center">
  
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

</div>

<div align="center">
  <img src="screenshot.png" alt="Simple Django Blog Screenshot" width="800px"/>
  <p><em>screenshot of the project</em></p>
</div>

## 📜 Overview

A straightforward, minimal blog platform built with the Django web framework. This project serves as a foundational example demonstrating core Django concepts, including models, the admin site, views, URL routing, templates, static/media file handling, with a touch of modern styling and responsive design.

It includes a robust user authentication system that allows users to create accounts, manage profiles, and author their own blog posts with full CRUD functionality. Users can also engage with content through a moderated commenting system and explore related content using the tag system.

It's designed to be easy to understand and extend, making it a great starting point for learning Django or showcasing web development skills.

## ✨ Features

### Core Features
- 📝 Create, view, and manage blog posts and categories
- 📄 Pagination for all listing pages (blog list, search results, user profiles)
- 🔍 Search for posts by title, content, author name, or tags
- 👤 Complete user authentication (register, login, logout)
- 👥 User profiles with customizable bio and profile picture
- 🔒 Permission-based access (only authors can edit their own posts)
- 📷 Upload and display images for each blog post
- 💬 Moderated commenting system with nested replies
- 🏷️ Tag system for organizing and discovering related content
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
- 📝 Create new posts with title, content, category, image, and tags
- ✏️ Edit your own posts
- 🗑️ Delete your own posts
- 👁️ View posts by specific authors
- 🏷️ Categorize posts for better organization
- 🔖 Add multiple tags to posts for more precise content organization

### Tag System
- 🏷️ Tag cloud displaying popular tags based on usage
- 🔍 Filter posts by clicking on tags
- 🔄 Related posts suggestion based on shared tags
- 📊 Tag cloud visualization with size based on popularity
- 🔠 Easy-to-use comma-separated tag input when creating/editing posts

### Search Functionality
- 🔍 Search for posts by title, content, author name, or tags
- 📊 Dedicated search results page with user-friendly layout
- 🔄 Search form accessible from any page in the header
- 💬 Clear feedback on search results and counts

### Comment System
- 💬 User commenting on blog posts
- 🧵 Threaded comments with reply functionality
- 👮 Comment moderation (admin approval required)
- 🗑️ Comment deletion (users can only delete their own comments)
- 👑 Admin control over all comments through the Django admin

### Pagination
- 📄 Post listings divided into manageable pages (6 posts per page)
- 🔢 Intuitive page navigation with first/previous/next/last controls
- 🔍 Maintains search parameters when navigating between results pages
- 📱 Responsive design that works on all device sizes
- 🧩 Consistent implementation across all listing views (blog list, profiles, search)


## 🛠️ Technologies Used

- **Backend**: Django (Python Web Framework)
- **Frontend**: HTML, CSS, JavaScript (for comment interactions)
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
5. Add tags to your post (comma-separated, e.g., "django, tutorial, web-development")
6. View your published content on the main site or your profile page

### Using Tags

The tag system allows for more granular content organization:

1. When creating or editing a post, add tags in the Tags field (separated by commas)
2. Tags will automatically be created if they don't exist
3. View the tag cloud on the main page to see popular tags
4. Click on any tag to see all posts with that tag
5. Related posts with similar tags appear on the post detail page

### Comment Moderation

By default, all comments require approval before being displayed:

1. Users can submit comments on any post after logging in
2. Comments are held for moderation and not displayed immediately
3. Site administrators can approve or reject comments through the admin interface
4. Only approved comments are displayed to all users
5. Users can only delete their own comments

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
│   ├── forms.py             # Forms for authentication, post management, comments, and search
│   ├── models.py            # Database models (Post, Category, UserProfile, Comment, Tag)
│   ├── tests.py             # Placeholder for app tests
│   ├── urls.py              # App-level URL patterns
│   └── views.py             # Logic to handle requests and return responses
├── templates/               # Project-level templates directory
│   └── blog/
│       ├── base.html        # Base template with navigation and common elements
│       ├── post_list.html   # Template for displaying list of posts
│       ├── post_detail.html # Template for displaying a single post with comments
│       ├── tag_posts.html   # Template for tag-filtered posts
│       ├── pagination.html  # Reusable pagination component
│       ├── register.html    # User registration form
│       ├── login.html       # User login form
│       ├── profile.html     # User profile management
│       ├── author_profile.html  # View another user's profile
│       ├── post_form.html   # Form for creating/editing posts
│       ├── post_confirm_delete.html # Confirmation for post deletion
│       ├── comment_confirm_delete.html # Confirmation for comment deletion
│       └── search_results.html # Display search results
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

- 📊 Analytics dashboard for tracking post views
- 📱 Social media sharing buttons
- 🔑 Social authentication options (Google, Facebook, etc.)
- 📧 Email subscription for blog updates
- 🌟 Comment rating/liking system
- 💻 Syntax highlighting for code snippets
- 📑 Post series/collections functionality
- 🗂️ Archive view by date
- 🔍 Advanced search with more filters
- 💾 Drafts and scheduled posts
- 🖋️ Rich text editor for post content
- 📱 RSS feed for post updates
- 🗳️ User voting/rating system for posts
- 🎯 Featured or sticky posts
- 📅 Editorial calendar for content planning

## 📜 License

This project is licensed under the MIT License.

---

<div align="center">
  <p>Made with ❤️ by <a href="https://github.com/ffiruzi">ffiruzi</a></p>
</div>