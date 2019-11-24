from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

from common.models import AppUsers
from django_hosts.resolvers import reverse


def corporate_check(user):
    if user.is_anonymous:
        return False
    else:
        return user.AppUsers.account_type == AppUsers.CORPORATE


@user_passes_test(corporate_check, login_url=reverse('corporate_login', host='common_urls'), redirect_field_name=None)  # TODO: Add decorator to all views
def corporate_home(request):
    return HttpResponse("corporate home")
