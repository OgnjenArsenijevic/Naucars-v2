from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django.urls import reverse
from PIL import Image


class Ad(models.Model):
    manufacturer = models.CharField(max_length=30)
    model = models.CharField(max_length=20)
    price = models.IntegerField(validators=[MaxValueValidator(50000000), MinValueValidator(1)])
    productionYear = models.IntegerField(validators=[MaxValueValidator(2019), MinValueValidator(1900)])
    color = models.CharField(null=True, blank=True, max_length=20)
    kilometers = models.IntegerField(null=True, blank=True, validators=[MaxValueValidator(2000000), MinValueValidator(1)])
    kW = models.IntegerField(null=True, blank=True, validators=[MaxValueValidator(7000), MinValueValidator(1)])
    cm3 = models.IntegerField(null=True, blank=True, validators=[MaxValueValidator(10000), MinValueValidator(1)])
    image = models.ImageField(default='default2.jpg', upload_to='car_pics')
    adOwner = models.ForeignKey(User, on_delete=models.CASCADE)
    contactNumber = models.CharField(max_length=15)
    datePosted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.manufacturer + ' ' + self.model

    def save(self, *args, **kwargs):
        super(Ad, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        height = img.height
        width = img.width
        minimum = min(height, width)

        if minimum == height:
            upper = 0
            lower = height
            offset = (width - 4*height/3) / 2
            left = offset
            right = offset + 4*height/3
            img = img.crop((left, upper, right, lower))
        elif minimum == width:
            offset = (height - width) / 2
            upper = offset
            lower = offset + width
            left = 0
            right = width
            img = img.crop((left, upper, right, lower))
        if img.width > 400 or img.height > 300:
            output_size = (400, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('ad-detail', kwargs={'pk': self.pk})
