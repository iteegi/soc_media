"""Forms for the accounts."""
from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    """User authorization form."""

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    """User registration form."""

    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        """Meta information."""

        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        """Check if both passwords match."""
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']
