from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
import signup


def login(request):
    if request.method == 'POST':
        first_name = request.POST["first_name"]
        password = request.POST["password"]
        user = auth.authenticate(first_name=first_name, password=password)

        if user is not None:
            auth.login(request, user)
            return  redirect('/')

        else:
            messages.info(request, "Invalid Login")
            return  redirect('login')
    return render(request, "login.html")


def signup(request):
    if request.method == 'POST':
        First_name = request.POST['First_name']
        Last_name = request.POST['Last_name']
        email = request.POST['email']
        Password = request.POST['Password']
        Confirm_Password = request.POST['Confirm_Password']
        if Password == Confirm_Password:
            if User.objects.filter(first_name=First_name).exists():
                messages.info(request, "First_name Existed")
                return  redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email Existed")
                return  redirect('signup')
            else:
                user = User.objects.create_user(username=First_name, first_name=First_name, last_name=Last_name,
                                                email=email)

                user.save();
                print("User Created")

                return  redirect('login')

        else:
            messages.info(request, "Password Incorrect")
            return redirect('signup')
        return  redirect('/')
    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return  redirect('/')
