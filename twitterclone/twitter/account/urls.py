from django.urls import path
from . import views


urlpatterns = [
    path('login/' , views.login , name='login'),
    path('register/' , views.userRegister , name='register'),
    path('logout/' , views.logout_request , name='logout')
]
    