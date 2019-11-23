from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

from E_Learning.common.models import Users


def manager_check(user):
    return user.users.account_type == Users.MANAGER


@user_passes_test(manager_check)  # TODO: Add decorator to all views
def manager_home(request):
    return HttpResponse("manager home")
