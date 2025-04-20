"""
Script to create a superuser for the admin panel.
Run this after setting up the project:
python manage.py shell < init_admin.py
"""

from django.contrib.auth.models import User

# Check if a superuser already exists
if not User.objects.filter(is_superuser=True).exists():
    User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='admin123',
        is_staff=True
    )
    print("Superuser created successfully!")
else:
    print("Superuser already exists.")