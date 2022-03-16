from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Youtuber(models.Model):
    youtuber = models.OneToOneField(User,on_delete=models.CASCADE)
    youtubeimage = models.ImageField(upload_to="ChannelPic")
    subscribers = models.ManyToManyField(User,blank=True,related_name="subs")
    channel_name = models.CharField(max_length=100)

class Video(models.Model):
    youtuber_video = models.ForeignKey(Youtuber,on_delete=models.CASCADE)
    video_thumbnail = models.ImageField(upload_to="thumbnails")
    video_title = models.CharField(max_length=255)
    video_desc = models.TextField()
    video = models.FileField(upload_to="videos")
    Views = models.IntegerField(null=True,blank=True,default=0)