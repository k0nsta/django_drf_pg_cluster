from rest_framework import serializers

from apps.library.models import Book
from apps.library.models import Reader


class BookBaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


class BookSerializer(BookBaseSerializer):

    class Meta(BookBaseSerializer.Meta):
        fields = ('id', 'title', 'isbn')


class ReaderBaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reader
        fields = ('id', 'name', 'username')


class ReaderSerializer(ReaderBaseSerializer):
    books = BookSerializer(many=True, required=False)

    class Meta(ReaderBaseSerializer.Meta):
        fields = ReaderBaseSerializer.Meta.fields + ('books', )
