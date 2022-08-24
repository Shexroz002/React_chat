from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    photo = models.ImageField(null=True,blank=True,upload_to='user_image/',default='user_image/userimage.jpg')
    chat_status = models.BooleanField(default=False)
    def __str__(self):
        return self.username


