# Local
from UserProfile.views import (SignupLowLeveUserView,
                               email_confirm_redirect,
                               password_reset_confirm_redirect)
# 3rd-party
from django.urls import path
from dj_rest_auth.registration.views import VerifyEmailView

urlpatterns = [
    path('verify-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
    path('account-confirm-email/<str:key>/', email_confirm_redirect, name="account_confirm_email"),
    path('password/reset/confirm/<str:uidb64>/<str:token>/', password_reset_confirm_redirect,
         name="password_reset_confirm"),
    # Not exposed for security Issues
    # path('', CustomSignupView.as_view(), name='custom_rest_register'),
    path('user/', SignupLowLeveUserView.as_view(), name='low_level_rest_register'),
    # path('org-user/', SignupLowestLeveUsers.as_view(), name='lowest_level_rest_register')
]
