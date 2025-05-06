from django.shortcuts import redirect
from django.views.generic import ListView, FormView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Image
from .forms import ImageCreateForm

class ImageDetailView(DetailView):
    model = Image
    template_name = 'images/image_detail.html'
    context_object_name = 'image'

class ImageListView(ListView):
    model = Image
    template_name = 'images/image_list.html'
    context_object_name = 'images'

class ImageCreateView(LoginRequiredMixin, FormView):
    template_name = 'images/image_create.html'
    form_class = ImageCreateForm

    def form_valid(self, form):
        new_image = form.save(commit=False)
        new_image.user = self.request.user 
        new_image.save()
        return redirect('image_list')
