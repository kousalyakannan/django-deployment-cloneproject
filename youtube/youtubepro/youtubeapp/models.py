from django.db import models
from django.utils import timezone
from django.urls import reverse


class Search(models.Model):
    title = models.CharField(max_length=200)
    searched_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
            return reverse('main',kwargs={'pk':self.pk})