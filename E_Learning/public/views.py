from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

from E_Learning.common.models import AppUsers


def public_check(user):
    return user.users.account_type == AppUsers.PUBLIC


@user_passes_test(public_check)  # TODO: Add decorator to all views
def public_home(request):
    return HttpResponse("public home")
