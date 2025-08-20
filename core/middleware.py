from django.shortcuts import redirect
from django.urls import reverse

class ForceProfileCompletionMiddleware:
    """
    Middleware to ensure users complete their profile before accessing certain views.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Skip middleware for unauthenticated users or certain paths
        exempt_paths = [
            reverse('login'),
            reverse('signup'), 
            reverse('verify_otp'),
            reverse('profile_completion'), 
            reverse('logout'),
            '/admin/'
        ]
        
        if request.user.is_authenticated and not request.user.is_profile_complete:
            # Don't redirect if user is on an exempt path
            if not any(request.path.startswith(path) for path in exempt_paths):
                return redirect('profile_completion')
        
        response = self.get_response(request)
        return response