# Create your tests here.
from django.test import TestCase, Client
from common.models import AppUsers, Companies
from django.contrib.auth.models import User

class AppUsersCreateTest(TestCase):
    def createPublic(self):
        c = Client()
        c.post("/account/public", {'username': ['test1'], 'email': ['a@b.com'], 'first_name': ['a'], 'last_name': ['b'], 'password': ['test1'], 'confirm': ['test1'], 'business_code': ['']})
        # username = "test1"
        # email = "a@b.com"
        # first_name = "a"
        # last_name = "b"
        # password = "pass1"
        # confirm = "pass1"
        # if password == confirm:
        #     user = User.objects.create_user(username, first_name=first_name, last_name=last_name, email=email,
        #                                     password=password)
        #     app_user = AppUsers(user=user, account_type="PUBLIC")
        #     app_user.save()
            
    def createCorporate(self):
        c = Client()
        c.post("/account/corporate", {'username': ['test2'], 'email': ['b@c.com'], 'first_name': ['b'], 'last_name': ['c'], 'password': ['test2'], 'confirm': ['test2'], 'business_code': ['code1']})
  