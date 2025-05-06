# Формы для регистрации и редактирования профиля

from django import forms
from django.contrib.auth.models import User
from .models import Profile

# Форма для регистрации нового пользователя
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)  # Поле для пароля
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)  # Проверка пароля

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']  # Поля для ввода

    def clean_password2(self):
        # Проверяем, что пароли совпадают
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return data['password2']

# Форма для редактирования пользователя
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'email']  # Редактируем имя и email

# Форма для редактирования профиля
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']  # Редактируем дату и фото