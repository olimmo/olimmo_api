from django.db.models.signals import post_save
from django.dispatch import receiver

from myapi.models import CustomUser, ExternalProperty, UserExternalProperty


@receiver(post_save, sender=ExternalProperty)
def create_user_external_property(sender, instance, created, **kwargs):
    if not created:
        return None

    for user in CustomUser.objects.all():
        user_exernal_property = UserExternalProperty(
            user=user, external_property=instance
        )
        user_exernal_property.clean_and_save()
