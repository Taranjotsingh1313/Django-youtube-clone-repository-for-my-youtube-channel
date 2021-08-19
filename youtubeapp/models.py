from django.db import models
from django.contrib.auth.models import User, update_last_login
# Create your models here.
class Youtuber(models.Model):
    youtuber = models.OneToOneField(User,on_delete=models.CASCADE)
    youtubeimage = models.ImageField(upload_to="ChannelPic")
    subscribers = models.ManyToManyField(User,blank=True,related_name="subs")
    channel_name = models.CharField(max_length=100)