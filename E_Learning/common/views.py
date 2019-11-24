from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import AppUsers
from .forms import LoginForm

    
# Create your views here.
def home(request):
    return render(request, "landing.html")


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
                    return redirect("public.osmith.me")
            else:
                form = LoginForm()
                return render(request, "error.html",
                              {"form": form, "account_type": "public"})  # todo: edit error.html and form

    else:
        form = LoginForm()
        return render(request, "login.html", {"form": form, "account_type": "public"})


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
                    return redirect("corporate.osmith.me")
            else:
                form = LoginForm()
                return render(request, "error.html",
                              {"form": form, "account_type": "corporate"})  # todo: edit error.html and form

    else:
        form = LoginForm()
        return render(request, "login.html", {"form": form, "account_type": "corporate"})


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
                    return redirect("manager.osmith.me")
            else:
                form = LoginForm()
                return render(request, "error.html", {"form": form})  # todo: edit error.html and form

    else:
        form = LoginForm()
        return render(request, "login.html", {"form": form})


def account_public(request):
    return HttpResponse("public account creation")  # TODO: Swap to web page


def account_corporate(request):
    return HttpResponse("corporate account creation")  # TODO: Swap to web page
