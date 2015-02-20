"""
Module contains views for user's authentication.
"""
from django.shortcuts import redirect
from django.contrib.auth import logout


def logout_view(request):
    """
    Logs student out.
    """
    logout(request)
    return redirect('/')
