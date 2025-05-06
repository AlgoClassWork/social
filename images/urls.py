from django.urls import path
from . import views


urlpatterns = [
    path('', views.ImageListView.as_view(), name='image_list'),
    path('detail/<int:id>/', views.ImageDetailView.as_view(), name='image_detail'),
    path('create/', views.ImageCreateForm.as_view(), name='image_create'),
]
