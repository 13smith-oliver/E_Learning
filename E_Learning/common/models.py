from django.db import models
from django.contrib.auth.models import User


class Companies(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)


class AppUsers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='+')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    company_id = models.ForeignKey(Companies, on_delete=models.SET_NULL, null=True)
    PUBLIC = "PUBLIC"
    CORPORATE = "CORPORATE"
    MANAGER = "MANAGER"
    ACCOUNT_TYPES = [(PUBLIC, 'Public'),
                     (CORPORATE, 'Corporate'),
                     (MANAGER, 'Manager')]
    account_type = models.CharField(max_length=9, choices=ACCOUNT_TYPES, default=PUBLIC,)

# TODO: finish making models
# TODO: make and apply migrations
