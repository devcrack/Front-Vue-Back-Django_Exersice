# 3rd-party
from django.contrib.auth.models import Group
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from dj_rest_auth.registration.views import RegisterView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Local
from an_api.base_permissions import HasGroupPermission
from UserProfile.serializers import (CustomUserSerializer,
                                     LowLevelUserSerializer,
                                     LowestLevelUserSerializer)


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


class SignupLowLeveUserView(RegisterView):
    serializer_class = LowLevelUserSerializer
    permission_classes = [IsAuthenticated, HasGroupPermission]

    def __get_group(self, group_name):
        return Group.objects.filter(name=group_name).first()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save(self.request)
        group = self.__get_group(serializer.validated_data.get('group'))
        user.groups.add(group)
        return Response(status=status.HTTP_201_CREATED)


class SignupLowestLeveUsers(SignupLowLeveUserView):
    required_groups = {'POST': ['manager', ]}
    serializer_class = LowestLevelUserSerializer


