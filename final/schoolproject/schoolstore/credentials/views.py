from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('store')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)

            user.save();
            return redirect('login')

        else:
            messages.info(request, "Password not matching")
            return redirect('register')
        return redirect('/')

    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def store(request):
    return render(request, "store.html")


def form(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        user = auth.authenticate(name=name, address=address)

        if user is not None:
            auth.login(request, user)
            return redirect('form')
        else:
            messages.info(request, "Order confirmed")
            return redirect('form')

    return render(request, "form.html")
