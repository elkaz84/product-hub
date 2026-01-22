# product_hub/signals.py
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.contrib import messages
from django.dispatch import receiver

@receiver(user_logged_in)
def on_user_logged_in(sender, request, user, **kwargs):
    # Add a friendly success message on login
    try:
        messages.success(request, f'Welcome back, {user.username}! You are now logged in.')
    except Exception:
        # If messages can't be added for some reason, silently ignore
        pass

@receiver(user_logged_out)
def on_user_logged_out(sender, request, user, **kwargs):
    # Add a success message on logout
    try:
        messages.success(request, 'You have successfully logged out.')
    except Exception:
        pass