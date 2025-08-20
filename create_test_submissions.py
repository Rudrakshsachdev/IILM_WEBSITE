#!/usr/bin/env python
"""
Create test submissions
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

from core.models import CustomUser, Submissions
from datetime import date

def create_test_submissions():
    print("Creating test submissions...")
    
    # Get the first user (or create one if none exists)
    try:
        user = CustomUser.objects.first()
        if not user:
            print("No users found. Creating a test user first...")
            user = CustomUser.objects.create_user(
                username='testuser',
                email='test@example.com',
                password='testpass123',
                is_profile_complete=True
            )
            print(f"Created user: {user.username}")
        
        # Create some test submissions
        submissions_data = [
            {'title': 'Research Paper on AI', 'status': 'submitted'},
            {'title': 'Conference Presentation', 'status': 'under_review'},
            {'title': 'Journal Article Draft', 'status': 'draft'},
            {'title': 'Patent Application', 'status': 'approved'},
            {'title': 'Book Chapter', 'status': 'returned'},
        ]
        
        for data in submissions_data:
            submission, created = Submissions.objects.get_or_create(
                user=user,
                title=data['title'],
                defaults={'status': data['status']}
            )
            if created:
                print(f"✓ Created submission: {submission.title}")
            else:
                print(f"- Submission already exists: {submission.title}")
        
        print(f"\nTotal submissions for {user.username}: {Submissions.objects.filter(user=user).count()}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    create_test_submissions()
