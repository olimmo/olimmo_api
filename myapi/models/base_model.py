from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    def clean_and_save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
