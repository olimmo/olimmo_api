from django.core.management.base import BaseCommand
from myapi.models import ExternalProperty, CustomUser
from myapi.tests.factories import ExternalPropertyFactory
import logging

logger = logging.getLogger(__name__)

MODE_REFRESH = "refresh"
MODE_CLEAR = "clear"


class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument("--mode", type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write("seeding data...")
        run_seed(self, options["mode"])
        self.stdout.write("done.")


def clear_data():
    print("Delete ExternalProperty instances")
    CustomUser.objects.all().delete()
    ExternalProperty.objects.all().delete()


def create_custom_users():
    print("Creating custom_users")
    CustomUser.objects.create_user("adrien.viv1@gmail.com", "password")
    CustomUser.objects.create_user("adrien.viv2@gmail.com", "password")
    print("custom_users created.")


def create_external_property():
    print("Creating external_property")
    external_property = ExternalPropertyFactory()
    print(f"external_property {external_property.id} created.")


def run_seed(self, mode):
    clear_data()
    if mode == MODE_CLEAR:
        return

    create_custom_users()
    for i in range(15):
        create_external_property()
