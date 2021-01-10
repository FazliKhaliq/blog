from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

from .forms import CreateUserForm

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created for ' + user)
        return redirect('../../')
    else:
            messages.info(request, 'Please Try Again')
    context = {'form': form}
    return render(request, 'register.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully Logged In')
            return redirect('../../blog/')
        else:
            messages.info(request, 'Username OR password is incorrect')
    return render(request, 'index.html')

def logoutUser(request):
    logout(request)
    messages.success(request, 'Successfully Logged out')
    return redirect('../../')