from django.urls import path

from api.v1.views import ReaderDetailView
from api.v1.views import CsvExportView

urlpatterns = [
    path(r'readers/<int:pk>', ReaderDetailView.as_view({'get': 'retrieve'})),
    path(r'export', CsvExportView.as_view()),
]
