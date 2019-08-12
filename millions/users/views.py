from django.shortcuts import render, redirect
from django.contrib import auth
from .models import User
from .forms import RegisterForm


def registerView(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            return redirect('/')
    else:
        user_form = RegisterForm()

    return render(request, 'registration/register.html', {'user_form': user_form})

def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'registration/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'registration/login.html')

def logoutView(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/')
    return render(request, 'registraion/register.html')
    



