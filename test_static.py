# create_dummy_user.py

import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Faculty_Portal.settings")
django.setup()

from core.models import CustomUser

# Only create if user with id=10 doesn't exist
if not CustomUser.objects.filter(id=10).exists():
    user = CustomUser(id=10, username='dummyuser10', email='dummy10@example.com')
    user.set_password('dummy123')  # Always use set_password to hash
    user.save()
    print("✅ Dummy user with ID 10 created.")
else:
    print("ℹ User with ID 10 already exists.")