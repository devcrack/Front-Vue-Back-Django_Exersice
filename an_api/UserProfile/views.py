# 3rd-party
from django.contrib.auth.models import Group
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from dj_rest_auth.registration.views import RegisterView
from rest_framework.response import Response
from rest_framework import status
# Local
from UserProfile.serializers import CustomUserSerializer, LowLevelUserSerializer


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


class SignupLowLeveUser(RegisterView):
    serializer_class = LowLevelUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = self.get_response_data(user)

        if data:
            response = Response(
                data,
                status=status.HTTP_201_CREATED,
                headers=headers,
            )
        else:
            response = Response(status=status.HTTP_204_NO_CONTENT, headers=headers)

        return response

