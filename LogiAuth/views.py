from django.shortcuts import render,redirect
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, LoginForm

# Create your views here.

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully for ' + form.cleaned_data['username'])
            return redirect('login')
    context = {'form': form}
    return render(request, 'accounts/register.html',context)

def loginPage(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html',{
        "form":form
    })

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


