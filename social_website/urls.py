# Главные маршруты сайта — какие страницы открывать

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Список маршрутов
urlpatterns = [
    path('admin/', admin.site.urls),            # Админ-панель
    path('account/', include('account.urls')),  # Маршруты для пользователей
    path('', include('images.urls')),           # Маршруты для изображений
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Доступ к медиа-файлам