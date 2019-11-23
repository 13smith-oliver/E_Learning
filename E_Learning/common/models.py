from django.db import models
from django.contrib.auth.models import User


class Companies:
    company_id = models.AutoField()
    name = models.CharField()


class Users:
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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
