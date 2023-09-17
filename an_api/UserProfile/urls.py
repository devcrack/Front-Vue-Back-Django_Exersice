# 3rd-party
from django.urls import path, include
from dj_rest_auth.registration.views import VerifyEmailView
from rest_framework.routers import SimpleRouter
# Local
from UserProfile.views import (SignupLowLeveUserView,
                               CustomUserListView,
                               email_confirm_redirect,
                               password_reset_confirm_redirect)

router = SimpleRouter()

router.register('users-list', CustomUserListView, basename='user-detail')

urlpatterns = [
    path('registration/verify-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
    path('registration/account-confirm-email/<str:key>/', email_confirm_redirect, name="account_confirm_email"),
    path('registration/password/reset/confirm/<str:uidb64>/<str:token>/', password_reset_confirm_redirect,
         name="password_reset_confirm"),
    # Not exposed for security Issues
    # path('', CustomSignupView.as_view(), name='custom_rest_register'),
    path('registration/user/', SignupLowLeveUserView.as_view(), name='low_level_rest_register'),
    path('', include(router.urls)),
]
