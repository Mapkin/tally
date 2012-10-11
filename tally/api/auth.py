from django.contrib.auth.models import User
from tally.api.models import Client


class ClientAuthentication(object):
    """Authenticate against the Client model."""

    def authenticate(self, username=None, password=None):
        """Authenticate the current user.

        Using ``username`` and ``password`` kwargs for compatibility with
        Tastypie's ``BasicAuthentication`` class.
        """
        try:
            client = Client.objects.get(api_key=username)
            return client.user
        except Client.DoesNotExist:
            pass
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
