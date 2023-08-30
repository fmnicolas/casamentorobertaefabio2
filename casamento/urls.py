from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rvsp.views import index
from rvsp.views import ConfirmacaoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'confirmacoes', ConfirmacaoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
