from django.contrib import admin
from django.urls import path, include
from slideshow.views import logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('slideshow.urls')),
    path('logout/', logout_view, name='logout'),
    path('', include('social_django.urls', namespace='social')),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)