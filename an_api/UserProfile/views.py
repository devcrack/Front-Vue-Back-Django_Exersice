# 3rd-party
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from dj_rest_auth.registration.views import RegisterView
from UserProfile.serializers import CustomUserSerializer

# Create your views here.


def email_confirm_redirect(request, key) -> HttpResponse:
    # return HttpResponseRedirect(
    #     f"{settings.EMAIL_CONFIRM_REDIRECT_BASE_URL}{key}/"
    # )
    return HttpResponse(f'Redirect to our nice Fronted page\n here is your Key for verified your email: {key}',
                        content_type='text/plain')


def password_reset_confirm_redirect(request, uidb64, token) -> HttpResponseRedirect:
    return HttpResponseRedirect(
        f"{settings.PASSWORD_RESET_CONFIRM_REDIRECT_BASE_URL}{uidb64}/{token}/"
    )


class CustomSignupView(RegisterView):
    serializer_class = CustomUserSerializer

