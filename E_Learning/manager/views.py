from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

from common.models import AppUsers


def manager_check(user):
    if user.user.is_anonymous:
        return False
    else:
        return user.users.account_type == AppUsers.MANAGER


@user_passes_test(manager_check)  # TODO: Add decorator to all views
def manager_home(request):
    return HttpResponse("manager home")
