from django.db import models
from django.contrib.auth.models import User

class Music(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='audio/')
    image_file = models.ImageField(upload_to='media/')  
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    listen_later_users = models.ManyToManyField(User, related_name='listen_later_songs', blank=True)

    def __str__(self):
        return self.title
