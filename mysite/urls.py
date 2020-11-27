from django.contrib import admin
from django.urls import path, include
from mysite import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('admin/', admin.site.urls),
    path('playlist/', include('playlist.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
