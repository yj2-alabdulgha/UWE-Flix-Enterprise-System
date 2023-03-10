from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login as login2, authenticate, logout as logout2
from django.http import HttpResponse
from .forms import *
# from .models import Customer

# Create your views here.


# def add_account(request):
#     form = CustomerForm(request.POST or None)
#     # student = Customer.objects.all()
#     if form.is_valid():
#         form.save()
#     return render(request, 'add.html', {'form': form})


# def show(request):
#     customer = Customer.objects.all()
#     return render(request, 'show.html', {'customer': customer})


# def update(request, id):
#     customer = Customer.objects.get(id=id)
#     form = CustomerForm(request.POST, instance=customer)
#     if form.is_valid():
#         form.save()  # Update Form
#         return HttpResponseRedirect('/')  # Redirects to View Page
#     return render(request, 'update.html', {'customer': customer})


# def delete(request, id):
#     form = Customer.objects.get(id=id)  # Grabs Current Form
#     form.delete()
#     return HttpResponseRedirect('/')

# Home View - Samuel


def home(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else: 
        return HttpResponseRedirect('/login')


# Login View - Samuel


def login(request):
    # If the request is POST, then the user has submitted the login form
    if request.method == 'POST':
        # Get the form
        form = LoginForm(request.POST)

        # Check if the form is valid
        if form.is_valid():
            # Clean the form data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Check if the login details are correct
            user = authenticate(username=username, password=password)

            # If the username/password is correct, log the user in
            if user is not None:
                login2(request, user)

                # Redirect User
                return HttpResponseRedirect('/home')
        else:
            # Returns an error message to the login page
            return render(request, 'login.html', {'form': LoginForm})

    # If the request is GET, then the user is requesting the login page
    else:
        # If the user is already logged in, redirect them to the home page
        if request.user.is_authenticated:
            return HttpResponseRedirect('/home')
        else:
            return render(request, 'login.html', {'form': LoginForm})

# Logout View - Samuel


def logout(request):
    # Check if the user is authenticated if so, log them out
    if request.user.is_authenticated:
        logout2(request)

    # Redirect to the login page
    return HttpResponseRedirect('/login')
