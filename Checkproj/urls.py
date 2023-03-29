from django.contrib import admin
from django.urls import path
from django.urls import path, include
from appcheck import urls as appcheck_urls
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(appcheck_urls, namespace="appcheck")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
