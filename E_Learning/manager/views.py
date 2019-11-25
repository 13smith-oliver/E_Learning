from django.shortcuts import redirect
from django.http import HttpResponse

from common.models import AppUsers


def manager_check(user): # TODO: Add check as function to all views
    if user.is_anonymous or user.AppUsers.account_type != AppUsers.MANAGER:
        return redirect('http://osmith.me/login/manager')
        

def manager_home(request):
    check = manager_check(request.user)
    if check is not None:
        return check
    return HttpResponse("manager home")
