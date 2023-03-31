from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login as login2, authenticate, logout as logout2
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import Film, FilmShowing
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

#Club Rep Showing View - Owain
def club_showings(request):
    film_title = request.POST.get('film_title')
    showings = FilmShowing.objects.filter(film=film_title)
    # Function to show showings only < club member amount
    return render(request, 'clubshowings.html', {'showings': showings})

# Home View - Samuel/Owain
@login_required(login_url='/login')
def home(request):
    films = Film.objects.all()
    return render(request, 'home.html', {'films': films})


# Generic Authentication Function
def authenticate_account(request):
    # Get the form
    form = LoginForm(request.POST)

    # Check if the form is valid

    if not form.is_valid():
        return None

    # Clean the form data
    username = form.cleaned_data['username']
    password = form.cleaned_data['password']

    # Check if the login details are correct
    user = authenticate(username=username, password=password)

    return user
        

# Customer Login View
def login(request):
    # If the request is POST, then the user has submitted the login form
    if request.method == 'POST':
        # Authenticate the user
        user = authenticate_account(request)

        # If the username/password is correct, log the user in

        if not user:
            return render(request, 'login/index.html', {'error': 'Invalid username and or password'})

        login2(request, user)

        # Redirect User
        return HttpResponseRedirect('/')


    # If the user is already logged in, redirect them to the home page
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    
    return render(request, 'login/index.html')
        

# Representative Login View
def representative_login(request):
    if request.method == 'POST':
        user = authenticate_account(request)

        if not user:
            return render(request, 'login/rep.html', {'error': 'Invalid username and or password'})
        
        login2(request, user)

        return HttpResponseRedirect('/')
    
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    
    return render(request, 'login/rep.html')

# Logout View - Samuel
def logout(request):
    # Check if the user is authenticated if so, log them out
    if request.user.is_authenticated:
        logout2(request)

    # Redirect to the login page
    return HttpResponseRedirect('/login')
