from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
#from datetime import datetime
#from home.models import Registration
from django.contrib import messages #for message or alaert after submit


# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        #Checkif user has entered correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")


def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/")
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

"""
def signupUser(request):
    if request.method == "POST":
        fullname = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        ##now, take an object registration of Registration
        registration = Registration(fullname = fullname, email=email, username=username, password=password, date=datetime.today())
        registration.save()
        messages.success(request, 'Your message has been sent!')
        return redirect("/login")
    return render(request, 'signup.html')
def signup_view(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'signup.html', {'form': form})
"""