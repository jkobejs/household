from django.shortcuts import redirect

# Create your views here.

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def login_view(request):

    print request.POST
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            if user.is_manager():
                return redirect('/household_manager/')
            else:
                return redirect('/transaction/')
        else:
            return redirect('/')
    else:
        return redirect('/')


def logout_view(request):
    logout(request)
    return redirect('/')
