# Common/Views.py

# Import Django libraries to authenticate user, log them in, and serve the web pages.
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django_hosts.resolvers import reverse

# Import classes from local models and forms to use in the views file
from common.models import AppUsers, Companies
from common.forms import LoginForm, CreateAccount


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
                if user.appuser.account_type == AppUsers.PUBLIC:
                    login(request, user)
                    # When the user is logged in, redirect to the public subdomain
                    return redirect("http://public.osmith.me")
                else:
                    return render(request, "login_error.html", {"form": form, "account_type": "public", "error_message": "domain_error"})  # TODO: Check webpage renders correctly
            else:
                form = LoginForm()
                return render(request, "login_error.html", {"form": form, "account_type": "public", "error_message": "incorrect"})  # TODO: Check error.html
        else:
            return render(request, "login_error.html", {"form": form, "account_type": "public", "error_message": "invalid"})  # TODO: Check webpage renders correctly
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
                if user.appuser.account_type == AppUsers.CORPORATE:
                    login(request, user)
                    # Redirect to corporate subdomain
                    return redirect("http://corporate.osmith.me")
                else:
                    return render(request, "login_error.html", {"form": form, "account_type": "corporate", "error_message": "domain_error"})  # TODO: Check webpage renders correctly
            else:
                form = LoginForm()
                return render(request, "login_error.html", {"form": form, "account_type": "corporate", "error_message": "incorrect"})  # TODO: Check error.html
        else:
            return render(request, "login_error.html", {"form": form, "account_type": "corporate", "error_message": "invalid"})  # TODO: Check webpage renders correctly
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
                if user.appuser.account_type == AppUsers.MANAGER:
                    login(request, user)
                    # Redirect to manager subdomain
                    return redirect("http://manager.osmith.me")
                else:
                    return render(request, "login_error.html", {"form": form, "account_type": "manager", "error_message": "domain_error"})  # TODO: Check webpage renders correctly
            else:
                form = LoginForm()
                return render(request, "login_error.html", {"form": form, "account_type": "manager", "error_message": "incorrect"})  # TODO: Check error.html
        else:
            return render(request, "login_error.html", {"form": form, "account_type": "manager", "error_message": "invalid"})  # TODO: Check webpage renders correctly
    else:
        form = LoginForm()
        return render(request, "login.html", {"form": form, "account_type": "manager"})

def account_public(request):
    if request.method == "POST":
        form = CreateAccount(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            password = form.cleaned_data["password"]
            confirm = form.cleaned_data["confirm"]
            if password == confirm:
                if User.objects.filter(username=username).exists():
                    return render(request, "account_error.html", {"form": form, "account_type": "public", "error_message": "username"})  # TODO: Check webpage renders correctly
                else:
                    user = User.objects.create_user(username, first_name=first_name, last_name=last_name, email=email,
                                                    password=password)
                    app_user = AppUsers(user=user, account_type="PUBLIC")
                    app_user.save()
                    login(request, user)
                    return redirect("http://public.osmith.me")
            else:
                return render(request, "account_error.html", {"form": form, "account_type": "public", "error_message": "passwords"})  # TODO: Check webpage renders correctly
        else:
            return render(request, "account_error.html", {"form": form, "account_type": "public", "error_message": "invalid"})  # TODO: Check webpage renders correctly
    else:
        form = CreateAccount()
        return render(request, "account.html", {"form": form, "account_type": "public"})


def account_corporate(request):
    if request.method == "POST":
        form = CreateAccount(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            password = form.cleaned_data["password"]
            confirm = form.cleaned_data["confirm"]
            business_code = form.cleaned_data["business_code"]
            if password == confirm:
                if User.objects.filter(username=username).exists():
                    return render(request, "account_error.html", {"form": form, "account_type": "corporate", "error_message": "username"})  # TODO: Check webpage renders correctly
                else:
                    user = User.objects.create_user(username, first_name=first_name, last_name=last_name, email=email,
                                                    password=password)
                    try:
                        company = Companies.objects.get(
                            business_code=business_code)  # TODO: Handle error from company not found
                    except Companies.DoesNotExist:
                        return render(request, "account_error.html", {"form": form, "account_type": "corporate", "error_message": "company"})

                    app_user = AppUsers(user=user, account_type="CORPORATE", company=company)
                    app_user.save()
                    login(request, user)
                    return redirect("http://corporate.osmith.me")
                    # TODO: Test Backend for account creation
            else:
                return render(request, "account_error.html", {"form": form, "account_type": "corporate", "error_message": "passwords"})  # TODO: Check webpage renders correctly
        else:
            return render(request, "account_error.html", {"form": form, "account_type": "corporate", "error_message": "invalid"})  # TODO: Check webpage renders correctly
    else:
        form = CreateAccount()
        return render(request, "account.html", {"form": form, "account_type": "corporate"})


def reset(request):
    User.objects.all().delete()
    AppUsers.objects.all().delete()
    
    user1 = User.objects.create_user("test1", first_name="a", last_name="b", email="a@b.com", password="test1")
    user2 = User.objects.create_user("test2", first_name="b", last_name="c", email="b@c.com", password="test2")
    user3 = User.objects.create_user("test3", first_name="c", last_name="d", email="c@d.com", password="test3")
    
    company = Companies.objects.get(business_code="code1")
    
    app_user1 = AppUsers(user=user1, account_type="PUBLIC")
    app_user1.save()
    
    app_user2 = AppUsers(user=user2, account_type="CORPORATE", company=company)
    app_user2.save()
    
    app_user3 = AppUsers(user=user3, account_type="MANAGER", company=company)
    app_user3.save()
    return HttpResponse("reset")