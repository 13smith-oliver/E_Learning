# Common/Forms.py

from django import forms


# Creates a form class that represents a form that can be used in a webpage. The Django Forms superclass adds methods
# to allow the form to be validated and cleaned.
class LoginForm(forms.Form):
    username = forms.CharField(label='Username', min_length=5, max_length=150)
    password = forms.CharField(label='Password', min_length=5, max_length=150, widget=forms.PasswordInput)


class CreateAccount(forms.Form):
    username = forms.CharField(label='Username', min_length=5, max_length=150)
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='First Name', min_length=1, max_length=30)
    last_name = forms.CharField(label='Last Name', min_length=1, max_length=150)
    password = forms.CharField(label='Password', min_length=5, max_length=150, widget=forms.PasswordInput)
    confirm = forms.CharField(label='Confirm Password', min_length=5, max_length=150, widget=forms.PasswordInput)
    businesscode = forms.CharField(label='Please enter your business code', min_length=5, max_length=5)