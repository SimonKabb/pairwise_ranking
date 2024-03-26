from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # Главная страница
    path('', views.upload_image, name='upload_image'),
    path('compare/', views.compare_images, name='compare_images'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
