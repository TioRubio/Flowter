from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='/media/default.jpg', upload_to='profile_pics')
    image_url = models.TextField(default='/media/default.jpg')

    def __str__(self):
        return f'{self.user.username} Profile'

    def get_username(self):
        return f'{self.user.username}'
    
    def get_email(self):
        return f'{self.user.email}'
