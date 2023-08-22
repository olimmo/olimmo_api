from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        included_field_names = self.get_included_fields()

        self.remove_unincluded_fields(representation, included_field_names)

        return representation

    def get_included_fields(self):
        included_fields_param = self.context["request"].query_params.get("included")
        if included_fields_param:
            return included_fields_param.split(",")
        return []  # No included fields by default

    def remove_unincluded_fields(self, representation, included_field_names):
        possible_included_fields = getattr(self.Meta, 'include_fields', [])

        for field_name in possible_included_fields:
            if field_name not in included_field_names:
                representation.pop(field_name, None)
