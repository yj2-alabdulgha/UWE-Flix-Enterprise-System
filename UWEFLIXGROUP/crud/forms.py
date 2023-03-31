from django import forms
from django.core.validators import FileExtensionValidator
#from datetime import datetime
#from datetime import date
#import time
#import calendar
#from django.core.exceptions import ValidationError
#from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator
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
#    def clean(self): ## Do not know if this works or not
#        tickets_for_adults = self.cleaned_data.get('tickets_for_adults')
#        tickets_for_students = self.cleaned_data.get('tickets_for_students')
#        tickets_for_children = self.cleaned_data.get('tickets_for_children')
#        if tickets_for_adults == 0 and tickets_for_students == 0 and tickets_for_children == 0:
#            raise forms.ValidationError("You must purchase one ticket to go forward")
#        return self.cleaned_data

#    def __movieticketchoices__(self, changevalue):
#        self.choose_payment_choices = changevalue

# Temprory forms for card payment details, might change as the development progresses.
#class CardForm(forms.Form):
#    present = date.present()
#    card_month = ()
#    card_year = ()
#    current_year = present.year
##Need to figure out how to put functionalities here for both selecting the date,month,year and also to input the card numbers.
#    Cnumber = forms.DecimalField(max_digits=16)
#    card_expiry_month = forms.ChoiceField(choices=card_month)
#    card_expiry_year = forms.ChoiceField(choices=card_year)

