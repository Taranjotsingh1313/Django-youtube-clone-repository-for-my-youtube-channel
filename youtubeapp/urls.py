from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.signup,name="signup"),
    path('login/',views.login1,name="login"),
    path('videoupload/',views.videoupload,name="uploadvideo"),
    path("video/",views.video,name="video"),
    path("createyoutuber/",views.youtuber,name="youtuber"),
]
