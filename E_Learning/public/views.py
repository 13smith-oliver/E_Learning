from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm


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
                if user.is_superuser:
                    login(request, user)
                    return redirect("/admin")
                elif user.is_staff:
                    login(request, user)
                    return redirect("/staff")
                else:
                    login(request, user)
                    return redirect("/students")

            else:
                form = LoginForm()
                return render(request, "error.html", {"form": form})

    else:
        form = LoginForm()
        return render(request, "login.html", {"form": form})
