#!/usr/bin/env python
import os
import django
from django.contrib.auth.models import User

# Setup Django environment
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_project.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()
from django.conf import settings
print(settings.INSTALLED_APPS,'azad')

from blog.models import Category, Tag, Blog, Comment

def create_sample_data():
    # Create categories
    tech_category = Category.objects.get_or_create(
        name="Technology",
        defaults={"description": "Posts about technology and programming"}
    )[0]

    lifestyle_category = Category.objects.get_or_create(
        name="Lifestyle",
        defaults={"description": "Posts about lifestyle and personal development"}
    )[0]

    # Create tags
    python_tag = Tag.objects.get_or_create(name="Python")[0]
    django_tag = Tag.objects.get_or_create(name="Django")[0]
    web_dev_tag = Tag.objects.get_or_create(name="Web Development")[0]
    tutorial_tag = Tag.objects.get_or_create(name="Tutorial")[0]

    # Create a test user (if admin doesn't exist)
    test_user = User.objects.get_or_create(
        username="testuser",
        defaults={
            "email": "test@example.com",
            "first_name": "Test",
            "last_name": "User"
        }
    )[0]

    # Create sample blog posts
    blog1 = Blog.objects.get_or_create(
        title="Getting Started with Django",
        slug="getting-started-with-django",
        defaults={
            "content": """Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel.

In this post, we'll cover the basics of Django and how to get started with your first Django project.

## What is Django?

Django is a free and open-source web framework written in Python. It follows the model-template-views (MTV) architectural pattern and is maintained by the Django Software Foundation.

## Key Features

- Fast development
- Secure by default
- Scalable
- Versatile
- Full-featured admin interface

## Getting Started

To get started with Django, you'll need Python installed on your system. Then you can install Django using pip:

```
pip install django
```

That's it! You're ready to create your first Django project.""",
            "author": test_user,
            "category": tech_category,
            "is_published": True
        }
    )[0]

    blog1.tags.add(python_tag, django_tag, web_dev_tag, tutorial_tag)

    blog2 = Blog.objects.get_or_create(
        title="Building a Blog with Django Models",
        slug="building-blog-django-models",
        defaults={
            "content": """In this tutorial, we'll learn how to create Django models for a blog application. We'll cover the essential relationships between models and best practices for structuring your data.

## Understanding Django Models

Django models are Python classes that define the structure of your database tables. Each model class represents a database table, and each attribute of the class represents a database field.

## Creating Blog Models

Let's start by creating our basic models:

### User Profile Model
We'll extend the built-in User model with a Profile model that has a one-to-one relationship.

### Blog Post Model
The main model for storing blog posts with fields for title, content, author, and publishing status.

### Category Model
For organizing blog posts into categories with a one-to-many relationship.

### Comment Model
For storing user comments on blog posts with support for nested replies.

This structure provides a solid foundation for a fully-featured blog application.""",
            "author": test_user,
            "category": tech_category,
            "is_published": True
        }
    )[0]

    blog2.tags.add(django_tag, tutorial_tag, python_tag)

    blog3 = Blog.objects.get_or_create(
        title="Tips for Better Work-Life Balance",
        slug="tips-better-work-life-balance",
        defaults={
            "content": """Achieving a healthy work-life balance is crucial for both personal well-being and professional success. Here are some practical tips to help you find that balance.

## Set Clear Boundaries

One of the most important steps is setting clear boundaries between work and personal time. This means:

- Having set work hours
- Not checking emails after work
- Creating a dedicated workspace at home
- Learning to say no to excessive demands

## Prioritize Self-Care

Taking care of yourself isn't selfish—it's necessary:

- Get adequate sleep (7-9 hours)
- Exercise regularly
- Eat nutritious meals
- Practice mindfulness or meditation
- Make time for hobbies and interests

## Time Management Strategies

Effective time management can help you be more productive during work hours:

- Use the Pomodoro Technique
- Prioritize tasks using the Eisenhower Matrix
- Minimize distractions
- Delegate when possible
- Take regular breaks

Remember, work-life balance looks different for everyone. Find what works for you and be willing to adjust as needed.""",
            "author": test_user,
            "category": lifestyle_category,
            "is_published": True
        }
    )[0]

    # Create sample comments
    Comment.objects.get_or_create(
        blog=blog1,
        author=test_user,
        defaults={"content": "Great introduction to Django! Very helpful for beginners."}
    )

    Comment.objects.get_or_create(
        blog=blog2,
        author=test_user,
        defaults={"content": "The model relationships explanation is very clear. Thanks!"}
    )

    print("Sample data created successfully!")
    print(f"Categories: {Category.objects.count()}")
    print(f"Tags: {Tag.objects.count()}")
    print(f"Blog posts: {Blog.objects.count()}")
    print(f"Comments: {Comment.objects.count()}")

if __name__ == "__main__":
    create_sample_data()