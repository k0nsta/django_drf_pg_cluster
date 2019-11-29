from django.db.models import CharField
from django.db.models import ManyToManyField

from core.models import BaseModel
from core.mixins import DateMixin
from core.mixins import IsActiveMixin


class Book(DateMixin, IsActiveMixin, BaseModel):
    SORT_SEQUENCE = ('id', 'title', 'isbn')

    class Meta:
        default_related_name = 'books'

    readers = ManyToManyField('Reader')
    title = CharField(max_length=512, blank=True)
    isbn = CharField(max_length=256, blank=True)

    def __str__(self):
        return f'Book(id={self.id}, title={self.title})'


class Reader(DateMixin, IsActiveMixin, BaseModel):
    SORT_SEQUENCE = ('id', 'name', 'username')

    class Meta:
        default_related_name = 'readers'

    name = CharField(max_length=64)
    username = CharField(max_length=64)

