from django.db import models


class DateMixin(models.Model):

    class Meta:
        abstract = True

    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)


class IsActiveMixin(models.Model):

    class Meta:
        abstract = True

    is_active = models.BooleanField(default=True)