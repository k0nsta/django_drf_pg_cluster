from django.http import StreamingHttpResponse

from rest_framework import views
from rest_framework import viewsets

from core.utils import CsvSerializer
from apps.library.models import Book
from apps.library.models import Reader
from api.v1.serializers import ReaderSerializer


class ReaderDetailView(viewsets.ReadOnlyModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer


class CsvExportView(views.APIView):

    def get(self, request):
        serializer = CsvSerializer()

        data = serializer.perform((Reader, Book))
        response = StreamingHttpResponse(
            serializer.yield_rows(data), content_type='text/csv'
        )
        response['Content-Disposition'] = 'attachment; filename="all.csv"'
        return response
