# Corporate/Views.py

# Import Django redirect to redirect the user. Import HttpResponse for testing purposes.
from django.http import HttpResponse
from django.shortcuts import redirect

# Import AppUsers model from the Common application.
from common.models import AppUsers


# The corporate_check function will check if the user is not logged in or if they are not a corporate user. If they are
# not, then they will be redirected to the corporate login page. If they are, the function will return None, else,
# it will return a redirect response object. This function can be added to all view functions within this file to
# check their authentication status.
def corporate_check(user):  # TODO: Add check as function to all views
    if user.is_anonymous or user.AppUsers.account_type != AppUsers.CORPORATE:
        return redirect('http://osmith.me/login/corporate')
    else:
        return None


# The corporate_home view will call the user check function to check whether the user is logged in. If they are not
# logged in, the view will return the redirect response to the user. If they are logged in, return the page they are
# looking for.
def corporate_home(request):
    check = corporate_check(request.user)
    if check is not None:
        return check
    # Response object for testing purposes.
    return HttpResponse("corporate home")  # TODO: Change to webpage
