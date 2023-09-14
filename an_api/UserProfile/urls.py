from UserProfile.views import (email_confirm_redirect,
                                      password_reset_confirm_redirect)
from django.urls import path

urlpatterns = [
    path('account-confirm-email/<str:key>/',
         email_confirm_redirect, name="account_confirm_email"),
    path(
        'password/reset/confirm/<str:uidb64>/<str:token>/',password_reset_confirm_redirect,
        name="password_reset_confirm"),

]

