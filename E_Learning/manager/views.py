# Manager/Views.py

# Import Django redirect to redirect the user. Import HttpResponse for testing purposes.
from django.shortcuts import redirect
from django.http import HttpResponse

# Import AppUsers model from the Common application.
from common.models import AppUsers


# The manager_check function will check if the user is not logged in or if they are not a manager user. If they are
# not, then they will be redirected to the manager login page. If they are, the function will return None, else,
# it will return a redirect response object. This function can be added to all view functions within this file to
# check their authentication status.
def manager_check(user):  # TODO: Add check as function to all views
    if user.is_anonymous:
        return redirect('http://osmith.me/login/manager')
    elif user.appuser.account_type != AppUsers.MANAGER:
        return redirect('http://osmith.me/login/manager')
    else:
        return None


# The manager_home view will call the user check function to check whether the user is logged in. If they are not
# logged in, the view will return the redirect response to the user. If they are logged in, return the page they are
# looking for.
def manager_home(request):
    check = manager_check(request.user)
    if check is not None:
        return check
    # Response object for testing purposes.
    return HttpResponse("manager home")  # TODO: Change to webpage
