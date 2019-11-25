from django.shortcuts import redirect
from django.http import HttpResponse

from common.models import AppUsers


def public_check(user):  # TODO: Add check as function to all views
    if user.is_anonymous or user.AppUsers.account_type != AppUsers.PUBLIC:
        return redirect('http://osmith.me/login/public')
    else:
        return None


def public_home(request):
    check = public_check(request.user)
    if check is not None:
        return check
    return HttpResponse("public home")
