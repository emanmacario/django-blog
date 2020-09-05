from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self, *args, **kwargs):
    #     """
    #     Overrides save method of Profile model, resizes user profile pictures
    #     """
    #     super().save(*args, **kwargs)

    #     im = Image.open(self.image.path)

    #     if im.height > 300 or im.width > 300:
    #         output_size = (300, 300)
    #         im.thumbnail(output_size, Image.ANTIALIAS)
    #         im.save(self.image.path)
