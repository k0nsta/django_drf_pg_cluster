from django.db import models

from core.utils import sorted_fields


class BaseModel(models.Model):
    SORT_SEQUENCE = tuple()

    class Meta:
        abstract = True

    @classmethod
    def get_sorted_fields(cls):
        fields = [f.name for f in cls._meta.fields]
        sorted_fields(fields, cls.SORT_SEQUENCE)
        return tuple(fields)
