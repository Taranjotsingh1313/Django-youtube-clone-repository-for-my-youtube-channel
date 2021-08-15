from django.contrib import admin
from .models import Youtuber
# Register your models here.
@admin.register(Youtuber)
class youtuber(admin.ModelAdmin):
    list_display = ['youtuber']