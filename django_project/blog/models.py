from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Each class is own table in database
# Each attribute is different field in database

# To make migrations, view SQL and run migrations:
# $ python manage.py makemigrations
# $ python manage.py sqlmigrate blog 0001
# $ python manage.py migrate

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Returns full path of post as a string
        return reverse('post-detail', kwargs={'pk': self.pk})

