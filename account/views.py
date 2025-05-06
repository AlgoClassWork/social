# Логика для страниц пользователей. Используем классы, как в книге

from django.views import View
from django.views.generic import TemplateView, FormView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import Profile, Contact
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from images.models import Image

# Личный кабинет (показывает ленту активности)
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'account/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        following_users = self.request.user.following.values_list('user_to', flat=True)
        context['images'] = Image.objects.filter(user__in=following_users) if following_users else []
        context['section'] = 'dashboard'
        return context

# Регистрация
class RegisterView(FormView):
    template_name = 'account/register.html'
    form_class = UserRegistrationForm

    def form_valid(self, form):
        # Сохраняем нового пользователя
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()
        Profile.objects.create(user=new_user)  # Создаём профиль
        return render(self.request, 'account/register_done.html', {'new_user': new_user})

# Редактирование профиля
class EditView(LoginRequiredMixin, TemplateView):
    template_name = 'account/edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Передаём формы для редактирования
        context['user_form'] = UserEditForm(instance=self.request.user)
        context['profile_form'] = ProfileEditForm(instance=self.request.user.profile)
        return context

    def post(self, request):
        # Обрабатываем отправку форм
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('dashboard')
        return render(request, 'account/edit.html', {
            'user_form': user_form,
            'profile_form': profile_form
        })

# Список пользователей
class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'account/user_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.exclude(id=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем информацию о подписках для каждого пользователя
        for user in context['users']:
            user.is_following = Contact.objects.filter(user_from=self.request.user, user_to=user).exists()
        return context

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User 
    template_name = 'account/user_detail.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = Image.objects.filter(user=self.get_object())
        return context
    
class UserFollowView(LoginRequiredMixin, View):
    def post(self, request):
        user_id = request.POST.get('id')
        action = request.POST.get('action')
        if user_id and action:
            user = User.objects.get(id=user_id)
            if action == 'follow':
                Contact.objects.get_or_create(user_from=request.user, user_to=user)
            elif action == 'unfollow':
                Contact.objects.filter(user_from=request.user, user_to=user).delete()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER','account/users/'))
        return HttpResponseRedirect('account/users/')