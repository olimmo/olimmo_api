# Load all models
import django
from django.apps import apps
from django.contrib.contenttypes.models import ContentType

from auditlog.models import LogEntry

django.setup()
all_models = apps.get_models()
for model in all_models:
    globals()[model.__name__] = model


# ------------------------------------
print("Welcome to Python!")

qq = exit

maison = ExternalProperty.objects.last()


# pluck(Property.objects.all(), 'title')
def pluck(objects, attribute):
    return list(map(lambda obj: getattr(obj, attribute), objects))


def audited(instance):
    content_type = ContentType.objects.get_for_model(instance)
    log_entries = LogEntry.objects.filter(
        content_type=content_type, object_pk=str(instance.pk), action=1
    )
    changes_list = []

    for log_entry in log_entries:
        changes = log_entry.changes_dict
        for field, (old, new) in changes.items():
            change_details = {
                "attribute": field,
                "previous_value": old,
                "new_value": new,
                "date": log_entry.timestamp,
            }
            changes_list.append(change_details)

    return changes_list
