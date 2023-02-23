from django.shortcuts import render
from .forms import CustomerForm
from .models import Customer
from django.http import HttpResponseRedirect

# Create your views here.
def add_account(request):
    form = CustomerForm(request.POST or None)
    #student = Customer.objects.all()
    if form.is_valid():
        form.save()
    return render(request, 'add.html', {'form': form})

def show(request):
    customer = Customer.objects.all()
    return render(request, 'show.html', {'customer': customer})

def update(request, id):
    customer = Customer.objects.get(id=id)
    form = CustomerForm(request.POST, instance=customer)
    if form.is_valid():
        form.save() # Update Form
        return HttpResponseRedirect('/') # Redirects to View Page
    return render(request, 'update.html', {'customer': customer})

def delete(request, id):
    form = Customer.objects.get(id=id) # Grabs Current Form
    form.delete()
    return HttpResponseRedirect('/')