"""
Defines urls patterns for Accounts.
"""
from django.urls import path, include
from . import views

# App
app_name = "accounts"

# Paths for each url

urlpatterns = [
    # Path for default authentication urls
    path("", include("django.contrib.auth.urls")),
    # Path for register a nre user
    path("register/", views.register, name="register")
]