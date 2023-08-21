import django_filters

from myapi.models import UserExternalProperty


class UserExternalPropertyFilter(django_filters.FilterSet):
    state = django_filters.CharFilter(field_name="state", lookup_expr="exact")

    class Meta:
        model = UserExternalProperty
        fields = ["state"]
