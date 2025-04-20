import os
import django
import sys

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')
django.setup()

# Import the User model after Django setup
from django.contrib.auth.models import User

def make_user_staff(username):
    try:
        user = User.objects.get(username=username)
        user.is_staff = True
        user.save()
        print(f"User '{username}' has been promoted to staff status.")
    except User.DoesNotExist:
        print(f"Error: User '{username}' does not exist.")
        return False
    return True

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python make_staff.py <username>")
        sys.exit(1)
    
    username = sys.argv[1]
    make_user_staff(username)