"""Authentication backend."""
from django.contrib.auth.models import User


class EmailAuthBackend(object):
    """Authenticates user by e-mail."""

    def authenticate(self, request, username=None, password=None):
        """Get user."""
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """Get user by ID."""
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
