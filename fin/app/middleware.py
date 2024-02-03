# middleware.py
from django.shortcuts import redirect
from django.urls import reverse

class LoginRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_paths = [reverse('login'), reverse('signup')]

        if not request.user.is_authenticated and not any(request.path.startswith(path) for path in allowed_paths):
            return redirect(reverse('login')) 

        response = self.get_response(request)
        return response
