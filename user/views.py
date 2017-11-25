from django.shortcuts import render
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .forms import LoginForm, SignUpForm
# Create your views here.

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('index')

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                django_login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                form.add_error(None, "Invalid username or password")
    
    else:
        form = LoginForm()

    return render(request, 'user/login.html', {'form': form })

def logout(request):
    django_logout(request)
    return render(request, "ai_index.html", {'user': request.user })

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            django_login(request, user)
            return render(request, "ai_index.html")
    else:
        form = SignUpForm()
    return render(request, "user/signup.html", {'form': form})
