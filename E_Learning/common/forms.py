# Common/Forms.py

from django import forms


# Creates a form class that represents a form that can be used in a webpage. The Django Forms superclass adds methods
# to allow the form to be validated and cleaned.
class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=35)
    password = forms.CharField(label='Password', max_length=35)
