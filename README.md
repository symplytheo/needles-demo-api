# Needles Demo API

A Django REST API for a blog platform with categories, posts, comments, and nested replies. Built with Django REST Framework and featuring custom JSON response formatting and pagination.

## Features

- **Blog Management**: Create, read, update, and delete blog posts
- **Category System**: Organize posts into categories with slug-based URLs
- **Comments & Replies**: Nested comment system with replies
- **Custom JSON Response**: Consistent API response format
- **Pagination**: Customizable pagination with page size controls
- **Admin Interface**: Django admin panel for content management
- **Slug Generation**: Automatic slug generation for posts and categories

## Tech Stack

- **Backend**: Django 4.2.24
- **API**: Django REST Framework 3.16.1
- **Database**: SQLite (development)
- **Code Formatting**: Black
- **Python**: 3.x

## Project Structure

```
needles_inks_api/
├── blog/                   # Blog app
│   ├── models.py          # Category, Post, Comment, Reply models
│   ├── serializers.py     # DRF serializers
│   ├── views.py           # API views
│   ├── urls.py            # Blog URL patterns
│   └── migrations/        # Database migrations
├── config/                # Project configuration
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL configuration
│   ├── helpers.py         # Custom renderers and pagination
│   └── wsgi.py            # WSGI configuration
├── db.sqlite3             # SQLite database
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
└── package.json           # NPM scripts for development
```

## API Endpoints

### Categories

- `GET /api/categories` - List all categories
- `POST /api/categories` - Create a new category

### Posts

- `GET /api/posts` - List all posts (paginated)
- `POST /api/posts` - Create a new post
- `GET /api/posts/<slug>` - Get post details by slug

### Comments

- `GET /api/comments` - List all comments
- `POST /api/comments` - Create a new comment

### Replies

- `POST /api/replies` - Create a reply to a comment

## Installation & Setup

### Prerequisites

- Python 3.x
- pip (Python package manager)

### 1. Clone the repository

```bash
git clone <repository-url>
cd needles_inks_api
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
# or using npm script
npm run install
```

### 4. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
# or using npm script
npm run migrate
```

### 5. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver 8001
# or using npm script
npm run dev
```

The API will be available at `http://localhost:8001/`

## API Response Format

All API responses follow a consistent format:

```json
{
  "success": true,
  "message": "Request completed successfully.",
  "data": {
    // Response data here
  },
  "errors": null
}
```

For paginated responses:

```json
{
  "success": true,
  "message": "Request completed successfully.",
  "data": {
    "items": [...],
    "meta": {
      "page": 1,
      "limit": 10,
      "total_pages": 5,
      "total_items": 50
    }
  },
  "errors": null
}
```

## Data Models

### Category

- `name`: Category name (unique)
- `slug`: URL-friendly slug (auto-generated)
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp

### Post

- `title`: Post title
- `slug`: URL-friendly slug (auto-generated)
- `content`: Post content
- `category`: Foreign key to Category
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp

### Comment

- `post`: Foreign key to Post
- `author`: Author name
- `message`: Comment content
- `created_at`: Creation timestamp

### Reply

- `comment`: Foreign key to Comment
- `author`: Author name
- `message`: Reply content
- `created_at`: Creation timestamp

## Development Scripts

The project includes npm scripts for common development tasks:

- `npm run dev` - Start development server on port 8001
- `npm run migrate` - Run makemigrations and migrate
- `npm run freeze` - Update requirements.txt with current packages
- `npm run install` - Install dependencies from requirements.txt
- `npm run generate <app_name>` - Generate a new Django app

## Admin Panel

Access the Django admin panel at `http://localhost:8001/admin/` to manage:

- Categories
- Posts
- Comments
- Replies
- User accounts

The admin interface is customized with "Needles And Inks" branding.
