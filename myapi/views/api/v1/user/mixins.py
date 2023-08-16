from rest_framework.exceptions import NotFound, ValidationError


from rest_framework.views import APIView

from myapi.models import CustomUser


class UserAuthenticationMixin(APIView):
    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

        uid = request.headers.get("Uid")
        if not uid:
            self.headers_error_response("Missing HTTP_UID header")

        self.current_user = CustomUser.objects.filter(email=uid).last()
        if not self.current_user:
            self.user_error_response()

    def headers_error_response(self, message):
        raise ValidationError({"detail": message})

    def user_error_response(self):
        raise NotFound({"detail": "User not found"})
