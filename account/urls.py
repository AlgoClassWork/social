from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('edit/', views.EditView.as_view(), name='edit'),
    path('users/', views.UserListView.as_view(), name='user_list'),
    #path('users/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    #path('users/follow/', views.UserFollowView.as_view(), name='user_follow'),
]