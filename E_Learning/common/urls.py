from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'', views.home, name='home'),
    url(r'/login/public', views.public_login, name='public_login'),
    url(r'/login/corporate', views.corporate_login, name='corporate_login'),
    url(r'/login/manager', views.manager_login, name='manager_login'),
    url(r'/account/public', views.account_public, name='account_public'),
    url(r'/account/corporate', views.account_corporate, name='account_corporate'),
]
