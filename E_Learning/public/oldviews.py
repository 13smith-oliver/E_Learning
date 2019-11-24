from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

from common.models import AppUsers


def public_check(user):
    if user.is_anonymous:
        return False
    else:
        return user.AppUsers.account_type == AppUsers.PUBLIC


@user_passes_test(public_check)  # TODO: Add decorator to all views
def public_home(request):
    return HttpResponse("public home")
