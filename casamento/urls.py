from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rvsp.views import index
from rvsp.consumers import Consumer

websocket_urlpatterns = [
    path('ws://casamentorobertaefabio2.vercel.app/', Consumer.as_asgi()),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('ws/', include(websocket_urlpatterns)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
