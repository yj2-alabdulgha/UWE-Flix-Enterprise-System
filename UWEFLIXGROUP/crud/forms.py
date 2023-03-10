from django import forms
# from .models import Customer

# class CustomerForm(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields = '__all__'

# Login Form
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
