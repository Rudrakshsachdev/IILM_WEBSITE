#!/usr/bin/env python
"""
Check existing users and create a test user
"""
import os
import sys
import django

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Faculty_Portal.settings')

# Setup Django
django.setup()

from core.models import CustomUser

def check_users():
    print("Checking existing users...")
    users = CustomUser.objects.all()
    
    if users.exists():
        print(f"Found {users.count()} users:")
        for user in users:
            print(f"  - {user.username} ({user.email}) - Profile Complete: {user.is_profile_complete}")
    else:
        print("No users found. Creating a test user...")
        try:
            # Create a test user
            user = CustomUser.objects.create_user(
                username='testuser',
                email='test@example.com',
                password='testpass123',
                is_profile_complete=True  # Set to True to avoid profile completion redirect
            )
            print(f"✓ Test user created: {user.username}")
            print("You can now login with:")
            print("Username: testuser")
            print("Password: testpass123")
        except Exception as e:
            print(f"✗ Failed to create test user: {e}")

if __name__ == "__main__":
    check_users()
