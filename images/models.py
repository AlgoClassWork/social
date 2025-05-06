from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='images_created'
    )
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title