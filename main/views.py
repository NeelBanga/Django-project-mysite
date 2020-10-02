from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Tutorials
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .form import NewUserForm
from django.contrib.auth.models import User,auth


# Create your views here.
def homepage(request):
    return render(request=request,
                  template_name="main/home.html",
                  context={"tutorials":Tutorials.objects.all})

def register(request):

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST['Email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,f"Username {username} already exists")
            elif User.objects.filter(email=email).exists():
                messages.error(request,"Email {email} already exists")
            else:
                user = User.objects.create_user(username=username,email=email,password=password1)
                messages.success(request, f"New account created: {username}")
                user.save()
                login(request,user)
                messages.info(request,f"You are now logged in as {username}")
                return redirect("main:homepage")
        else:
            #for msg in form.error_messages:
            messages.error(request, "Password not matching")
        '''form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request,user)
            messages.info(request,f"You are now logged in as {username}")
            return redirect("main:homepage")'''


    #form = NewUserForm()
    return render(request,
                  "main/register.html")

def logout_request(request):
    logout(request)
    messages.info(request,f"You are logged out successfully")
    return redirect("main:homepage")


def login_request(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            messages.info(request, f"You are now logged in as {username}")
            return redirect("main:homepage")
        else:
            messages.info(request,"invalid credentials")


        '''form = AuthenticationForm(request, data=request.POST)
        if form.is_valid:
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.info(reqestt, f"You are now logged in as {username}")
                return redirect("main:homepage")
            else:
                messages.error(request,f"Invalid username or password")
        else:
            messages.error(request,f"Invalid username or password")'''


    #form = AuthenticationForm()
    return render(request,"main/login.html")