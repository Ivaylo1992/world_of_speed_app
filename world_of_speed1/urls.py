from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("world_of_speed1.web.urls")),
    path("profile/", include("world_of_speed1.profiles.urls")),
    path("cars/", include("world_of_speed1.cars.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

