from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate 
from .models import Youtuber
# Create your views here.
def index(request):
    return render(request,'youtubeapp/index.html')

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
    return render(request,'youtubeapp/videoupload.html',{})

def video(request):
    return render(request,'youtubeapp/video.html',{})

# CREATE USER A YOUTUBER FUNCTION
def youtuber(request):
    check = Youtuber.objects.filter(youtuber=request.user)
    if not check:
        youtuber = Youtuber.objects.create(youtuber=request.user)
        if youtuber:
            return redirect("uploadvideo")
    else:
        return redirect("index")

    return HttpResponse("YOUTUHOOBER CREATED")