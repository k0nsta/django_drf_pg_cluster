from django.contrib import admin
from django.urls import path
from django.urls import include

from api.v1.urls import urlpatterns as api_v1


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_v1))
]
