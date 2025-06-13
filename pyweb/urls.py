from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from CRUD.views import custom_404_view  # replace yourapp with your actual app name

handler404 = custom_404_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("CRUD.urls")),
    path('blogs/', include("CRUD.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
