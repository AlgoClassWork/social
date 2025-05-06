from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'Профиль {self.user.username}'

class Contact(models.Model):
    user_from = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE
    )
    user_to = models.ForeignKey(
        User, related_name='followers', on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return f'{self.user_from} подписан на {self.user_to}'