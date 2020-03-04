"""Admin."""
from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile model registration in admin panel."""

    list_display = ['user', 'date_of_birth', 'photo']
