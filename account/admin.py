# Настройки админ-панели для управления профилями и подписками

from django.contrib import admin
from .models import Profile, Contact

# Регистрируем профиль
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth']  # Показываем пользователя и дату рождения
    list_filter = ['date_of_birth']          # Фильтр по дате

# Регистрируем подписки
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['user_from', 'user_to', 'created']  # Показываем, кто на кого подписан