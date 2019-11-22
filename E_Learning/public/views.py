from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from common.forms import LoginForm


# Create your views here.
def public_home(request):
    # return HttpResponse("public home")
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                # TODO: Change the checking to check account type (public, corporate, manager)
                if user.is_superuser:
                    login(request, user)
                    return redirect()  # TODO: Edit redirect links
                elif user.is_staff:
                    login(request, user)
                    return redirect("/staff")
                else:
                    login(request, user)
                    return redirect("/students")

            else:
                form = LoginForm()
                return render(request, "error.html", {"form": form})  # todo: edit error.html and form

    else:
        form = LoginForm()
        return render(request, "login.html", {"form": form})
