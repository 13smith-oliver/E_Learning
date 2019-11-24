from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django_hosts.resolvers import reverse

from common.models import AppUsers


def manager_check(user):
    if user.is_anonymous:
        return False
    else:
        return user.AppUsers.account_type == AppUsers.MANAGER


@user_passes_test(manager_check, login_url=reverse('manager_login', host='common_urls'), redirect_field_name=None)  # TODO: Add decorator to all views
def manager_home(request):
    return HttpResponse("manager home")
