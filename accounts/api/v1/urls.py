from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import signup

app_name = 'accounts-rest-v1'

urlpatterns = [
    path('login', obtain_auth_token),
    path('signup', signup)
]