from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.signup,name="signup"),
    path('login/',views.login1,name="login"),
    path('videoupload/',views.videoupload,name="uploadvideo"),
    path('youtuber/',views.youtuber,name="youtuber"),
    path("video/<int:id>/",views.video,name="video"),
    path("createchannel/",views.create_channel,name="create_channel"),
    path('channel/',views.channel,name="channel"),
    path('subscribe/<int:id>/',views.subscribe,name="subscribe"),
    path("user/<int:id>/",views.anychannel,name="user_channel")
]
