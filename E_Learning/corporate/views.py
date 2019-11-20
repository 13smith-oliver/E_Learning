from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def corporate_home(request):
    return HttpResponse("corporate home")
