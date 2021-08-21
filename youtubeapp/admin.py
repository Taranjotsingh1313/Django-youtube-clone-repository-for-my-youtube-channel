from django.contrib import admin
from .models import Video, Youtuber
# Register your models here.
@admin.register(Youtuber)
class youtuber(admin.ModelAdmin):
    list_display = ['youtuber']

@admin.register(Video)
class youtuber(admin.ModelAdmin):
    list_display = ['id','youtuber_video']