from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.views import APIView
from myapi.models import UserExternalProperty, CustomUser


class UserAuthenticationMixin(APIView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.current_user = None
        self.current_user_external_properties = None

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

        self.current_user = self._get_current_user(request)
        self.current_user_external_properties = (
            self._get_current_user_external_properties(self.current_user)
        )

    def _get_current_user(self, request):
        uid = request.headers.get("Uid")
        if not uid:
            raise ValidationError({"detail": "Missing HTTP_UID header"})

        current_user = CustomUser.objects.filter(email=uid).last()
        if not current_user:
            raise NotFound({"detail": "User not found"})

        return current_user

    def _get_current_user_external_properties(self, current_user):
        return UserExternalProperty.objects.filter(user=current_user)
