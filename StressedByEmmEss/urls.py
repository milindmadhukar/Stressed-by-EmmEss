from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Stresses By EmmEss Administartion"
admin.site.site_title = "Stresses By EmmEss Admin Panel"
admin.site.index_title = "Welcome to Stresses By EmmEss Panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('menu/', include('menu.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)