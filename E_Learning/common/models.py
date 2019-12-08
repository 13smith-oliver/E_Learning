# Common/Models.py

from django.db import models
# Import Django default user for use in Foreign Key relationships.
from django.contrib.auth.models import User


# Create a model called Companies, which will create a companies table in the database.
class Companies(models.Model):
    # Create a custom Primary Key field, with the name company_id.
    company_id = models.AutoField(primary_key=True)
    # Create a character field called name, with a maximum length of 50 characters.
    name = models.CharField(max_length=50)
    businesscode = models.CharField(max_length=5)


# Create a model called AppUsers, which will create an appusers table in the database which will extend the number of
# details that the system will store about the users.
class AppUsers(models.Model):
    # Create a One to One relationship with the default User.
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='+')
    # Creates a Foreign Key linking to User so that if the user is created by a manager, the system will know who
    # made the account.
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # Creates a Foreign Key to
    company_id = models.ForeignKey(Companies, on_delete=models.SET_NULL, null=True)
    PUBLIC = "PUBLIC"
    CORPORATE = "CORPORATE"
    MANAGER = "MANAGER"
    ACCOUNT_TYPES = [(PUBLIC, 'Public'),
                     (CORPORATE, 'Corporate'),
                     (MANAGER, 'Manager')]
    account_type = models.CharField(max_length=9, choices=ACCOUNT_TYPES, default=PUBLIC, )

# TODO: finish making models
# TODO: make and apply migrations
