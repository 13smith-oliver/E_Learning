# Common/Views.py

# Import Django libraries to authenticate user, log them in, and serve the web pages.
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Import classes from local models and forms to use in the views file
from .models import AppUsers
from .forms import LoginForm, CreateAccount


# Home view that renders the landing page. Rendering will take the template and substitute any necessary code and
# return a html file
def home(request):
    return render(request, "landing.html")


# Public Login view that will return the login form and will change the login.html file because the account_type
# variable is "public". If the request method is POST (which is how the system sends data to the server),
# the view will instead treat the data as if the user has already received the page and is now sending data to the
# server, i.e. the user has submitted a login form. If request.method equals POST, then the server will build an
# object from the data with a LoginForm (common/forms.py), which will validate the data and clean it up. The server
# will then authenticate the user, which checks if the username and password combination is valid. If it is,
# then it will log the user in and redirect them to the public homepage. If not then it will return an error page,
# which is the login page with a block that contains an error message as well.
def public_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.users.account_type == AppUsers.PUBLIC:
                    login(request, user)
                    # When the user is logged in, redirect to the public subdomain
                    return redirect("public.osmith.me")
            else:
                form = LoginForm()
                return render(request, "error.html", {"form": form, "account_type": "public"})
    else:
        form = LoginForm()
        return render(request, "login.html", {"form": form, "account_type": "public"})


# The Corporate Login view works the same way as the Public View but logs the user into the Corporate subdomain
# instead of the Public subdomain.
def corporate_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.users.account_type == AppUsers.CORPORATE:
                    login(request, user)
                    # Redirect to corporate subdomain
                    return redirect("corporate.osmith.me")
            else:
                form = LoginForm()
                return render(request, "error.html", {"form": form, "account_type": "corporate"})
    else:
        form = LoginForm()
        return render(request, "login.html", {"form": form, "account_type": "corporate"})


# The Manager Login view works the same way as the Public View but logs the user into the Manager subdomain
# instead of the Public subdomain.
def manager_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.users.account_type == AppUsers.MANAGER:
                    login(request, user)
                    # Redirect to manager subdomain
                    return redirect("manager.osmith.me")
            else:
                form = LoginForm()
                return render(request, "error.html", {"form": form})
    else:
        form = LoginForm()
        return render(request, "login.html", {"form": form})


def account_public(request):
    if request.method == "POST":
        form = CreateAccount(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]  # TODO: Add Backend for account creation
            
    else:
        form = CreateAccount()
        return render(request, "account.html", {"form": form, "account_type": "public"})

def account_corporate(request):
    if request.method == "POST":
        form = CreateAccount(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]  # TODO: Add Backend for account creation
            
    else:
        form = CreateAccount()
        return render(request, "account.html", {"form": form, "account_type": "corporate"})

