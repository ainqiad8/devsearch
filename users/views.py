from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth.models import User
from .models import Profiles
from . forms import CustomUserCreationForm
# Create your views here.


def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, "username does not exist")
        
        user = authenticate(request, username=username, password=password)


        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, "username or password is incorrect")

    return render(request, "users/login_register.html")


def logoutUser(request):
    logout(request)
    messages.error(request, "user was logged out")
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "USER is created")

            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'an error has occurred during registration')

            
        

            
    context = {
        'page':page,
        'form':form,
    }
    return render(request, 'users/login_register.html', context)



def profiles(request):
    profile = Profiles.objects.all()
    context = {
        "profiles":profile
    }
    return render(request, 'users/profiles.html', context)


def userprofile(request, pk):
    profile = Profiles.objects.get(id=pk)

    topskills = profile.skill_set.exclude(description__exact="")
    otherskills = profile.skill_set.filter(description="")


    context = {
        "profile":profile,
        'topskills': topskills,
        'otherskills': otherskills,
    }
    return render(request, 'users/user-profile.html', context) 