from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default1.jpg', upload_to='profile_pics')
    name = models.CharField(default='Name', max_length=20)
    surname = models.CharField(default='Surname', max_length=50)
    phone = models.CharField(default='Phone number', max_length=15)

    def __str__(self):
        return f'{self.user.username} Profile '

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.width > 300 or img.height > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
