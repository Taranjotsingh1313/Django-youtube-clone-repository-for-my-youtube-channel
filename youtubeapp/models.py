from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Youtuber(models.Model):
    youtuber = models.OneToOneField(User,on_delete=models.CASCADE)