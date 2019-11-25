from django.http import HttpResponse
from django.shortcuts import redirect

from common.models import AppUsers


def corporate_check(user): # TODO: Add check as function to all views
    if user.is_anonymous or user.AppUsers.account_type != AppUsers.CORPORATE:
        return redirect('http://osmith.me/login/corporate')


def corporate_home(request):
    check = corporate_check(request.user)
    if check is not None:
        return check
    return HttpResponse("corporate home")
