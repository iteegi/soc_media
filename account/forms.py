"""Forms for the accounts."""
from django import forms


class LoginForm(forms.Form):
    """User authorization form."""

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
