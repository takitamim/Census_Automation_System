from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

class EmailBackend(ModelBackend):
    """
    Custom authentication backend that allows users to log in using their email address.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Try to find a user with the given email
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return None
        
        # Check the password
        if user.check_password(password):
            return user
        return None