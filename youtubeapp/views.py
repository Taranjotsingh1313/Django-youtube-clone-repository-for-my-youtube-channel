from django.http import JsonResponse
from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate 
from .models import Video, Youtuber
# Create your views here.
def index(request):
    context = {}
    if request.user.is_authenticated:
        youtuber  = Youtuber.objects.filter(youtuber=request.user)
        if youtuber:
            context = {"success":"hai"}
    return render(request,'youtubeapp/index.html',context)

def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        cpass = request.POST['cpassword']
        if cpass != password:
            messages.warning(request,'''Password Doesn't match ''')
            return redirect("signup")
        else:
            if email and username and password:
                a = User.objects.create_user(username,email,password)
                if a:
                    messages.success(request,'Please Login And You are now member of our family')
                    return redirect('login')
    return render(request,'youtubeapp/signup.html',{})

def login1(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect("index")
        else:
            messages.warning(request,'Please First Create Account or Account Details are wrong')
            return redirect('login')
    return render(request,"youtubeapp/login.html")

def videoupload(request):
    context ={}
    youtuber = Youtuber.objects.filter(youtuber=request.user)
    if youtuber:
        context = {"success":"hai"}
    if request.method == 'POST':
        video_title = request.POST['videoTitle']
        video = request.FILES['video']
        video_thumbnail = request.FILES['thumbnail']
        video_desc = request.POST['description']
        youtuber_video = Youtuber.objects.filter(youtuber=request.user)[0]
        if youtuber_video:
            video = Video.objects.create(youtuber_video=youtuber_video,video_thumbnail=video_thumbnail,video_title=video_title,video=video,video_desc=video_desc)
            if video:
                context = {'uploaded':True}
    return render(request,'youtubeapp/videoupload.html',context)

def video(request):
    context ={}
    youtuber = Youtuber.objects.filter(youtuber=request.user)
    if youtuber:
        context = {"success":"hai"}
    return render(request,'youtubeapp/video.html',context)

# CREATE USER A YOUTUBER FUNCTION
def youtuber(request):
    check = Youtuber.objects.filter(youtuber=request.user)
    if not check:
        youtuber = Youtuber.objects.create(youtuber=request.user)
        if youtuber:
            return redirect("create_channel")
    else:
        return redirect("index")

    return HttpResponse("YOUTUHOOBER CREATED")

def create_channel(request):
    if request.method == 'POST':
        file = request.FILES['file']
        channelname = request.POST['channelname']
        youtuber = Youtuber.objects.filter(youtuber=request.user).update(channel_name=channelname,youtubeimage=file)
        if youtuber:
            return JsonResponse({
                'success':True,
                'link':'channel/'
            })
    context ={}
    youtuber = Youtuber.objects.filter(youtuber=request.user)
    if youtuber:
        context = {"success":"hai"}
    return render(request,'youtubeapp/createchannel.html',context)

def channel(request):
    context ={}
    youtuber = Youtuber.objects.filter(youtuber=request.user)
    if youtuber:
        context = {"success":"hai"}
    return render(request,'youtubeapp/channel.html',context)