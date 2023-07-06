# Load all models
import django
from django.apps import apps
django.setup()
all_models = apps.get_models()
for model in all_models:
    globals()[model.__name__] = model

# ------------------------------------
print("Welcome to Python!")

maison = Property.objects.get(id=1)
qq = exit
