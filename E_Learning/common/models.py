from django.db import models
from django.contrib.auth.models import User

class Companies:
    company_id = models.AutoField()
    name = models.CharField()
    
class Users:
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    company_id = models.ForeignKey(Companies, on_delete=models.SET_NULL, null=True)
    account_type = models.CharField()

