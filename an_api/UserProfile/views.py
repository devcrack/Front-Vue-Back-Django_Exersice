# 3rd-party
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse


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
