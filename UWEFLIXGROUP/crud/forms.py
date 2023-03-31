from django import forms
from django.core.validators import FileExtensionValidator
# from .models import Customer

# class CustomerForm(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields = '__all__'

# Login Form
class LoginForm(forms.Form):
    email = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)

# Screen Booking/Showing Form - Customer
class ShowingForm(forms.Form):
    film = forms.IntegerField()
    screen = forms.IntegerField()
    film_date = forms.DateInput()
    ticket_quantity = forms.IntegerField()

class CustomerForm(forms.Form):
    title = forms.CharField(max_length=4)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    email = forms.EmailField()
    date_of_birth = forms.DateField()

class FilmForm(forms.Form):
    title = forms.CharField(max_length=100)
    rating = forms.ChoiceField(choices=[('U', 'U'), ('PG', 'PG'), ('12A', '12A'), ('15', '15'), ('18', '18')])
    duration = forms.IntegerField(min_value=1)
    description = forms.CharField(max_length=500)
    image = forms.ImageField(allow_empty_file=False, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])], widget=forms.FileInput)
    trailer = forms.URLField()

# Temprory forms for transaction might need to change it as it progresses - Anushka
# class UWEPaymentForm(forms.Form):
#    tickets_for_adults = forms.IntegerField(validators=[ MaxValueValidator(100), MinValueValidator(0)],required=False, initial=0)
#    tickets_for_students = forms.IntegerField(validators=[ MaxValueValidator(100), MinValueValidator(0)],required=False, initial=0)
#    tickets_for_children = forms.IntegerField(validators=[ MaxValueValidator(100), MinValueValidator(0)],required=False, initial=0)
#    cost_of_all_tickets=forms.FloatField(label="Cost of Total Tickets: ", disabled=True, required=False)
#    choose_payment_choices = [(None, 'Select an option:'), ('CPay', 'Customer: Pay with Card'), ('SPay', 'Student: Pay with Credit'), ]