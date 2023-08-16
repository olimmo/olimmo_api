from django.db import models

from django.core.validators import MinLengthValidator

from . import BaseModel


class UserExternalProperty(BaseModel):
    STATE_CHOICES = [
        ("contacted", "Contacted"),
        ("rejected", "Rejected"),
        ("waiting", "Waiting"),
    ]

    state = models.CharField(
        choices=STATE_CHOICES,
        max_length=10,
        validators=[MinLengthValidator(1)],
        default="waiting",
    )

    # Relationships
    user = models.ForeignKey(
        "myapi.CustomUser", on_delete=models.CASCADE, blank=False, null=False
    )
    external_property = models.ForeignKey(
        "myapi.ExternalProperty", on_delete=models.CASCADE, blank=False, null=False
    )

    def __str__(self):
        return str(vars(self))

    class Meta:
        unique_together = ["user", "external_property"]
