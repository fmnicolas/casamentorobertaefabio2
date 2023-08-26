from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rvsp.views import index
from rvsp import websocket_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
]

urlpatterns += [
    path('ws/', include(websocket_urlpatterns)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
