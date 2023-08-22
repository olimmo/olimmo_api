import django_filters

from myapi.models import UserExternalProperty


class UserExternalPropertyFilter(django_filters.FilterSet):
    state = django_filters.CharFilter(field_name="state", lookup_expr="exact")
    order_by = django_filters.OrderingFilter(fields=("created_at",))

    class Meta:
        model = UserExternalProperty
        fields = ["state"]
