from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from myapi.models import Seller


class BaseView(APIView):
    def current_seller(self, seller_id):
        return get_object_or_404(Seller, pk=seller_id)
