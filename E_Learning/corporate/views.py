from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

from E_Learning.common.models import Users


def corporate_check(user):
    return user.users.account_type == Users.CORPORATE


@user_passes_test(corporate_check)  # TODO: Add decorator to all views
def corporate_home(request):
    return HttpResponse("corporate home")
