from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', include('store.urls')),
    path('order/', include('order.urls')),
    path('payment/', include('payment.urls')),
    path('notification/', include('notification.urls'),)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)