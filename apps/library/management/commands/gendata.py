import random

from mixer.backend.django import Mixer

from django.core.management.base import BaseCommand

from apps.library.models import Book
from apps.library.models import Reader


class Command(BaseCommand):
    help = "Load fake test data"

    def handle(self, *args, **options):
        batch_size = 5000
        book_cap, reader_cap = 100000, 50000
        mixer = Mixer(commit=False)

        books = mixer.cycle(book_cap).blend(Book)
        readers = mixer.cycle(reader_cap).blend(Reader)

        for i in range(0, reader_cap, batch_size):
            Reader.objects.bulk_create(readers[i:i + batch_size])

        for i in range(0, len(books), batch_size):
            Book.objects.bulk_create(books[i:i + batch_size])

        for book in books:
            index = random.randrange(1, reader_cap)
            book.readers.add(readers[index])
