from django.shortcuts import render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from profiles.models import Profiles # مدل پروفایل کاربران
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

# Create your views here.

def home(request):
   return render(request,'firstpage.html')
def mylogin_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('karino')
        else:
            return render(request, 'main/login.html', {'error': 'نام کاربری یا رمز اشتباه است'})
    return render(request, 'main/login.html')

def karino_view(request):
    return render(request, "main/karino.html")
   
@csrf_exempt
def myregister_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone_number = request.POST.get("phone_number")

        # بررسی تکراری بودن نام کاربری یا ایمیل
        if User.objects.filter(username=username).exists():
            messages.error(request, "این نام کاربری قبلاً ثبت شده است.")
            return render(request, 'main/register.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "این ایمیل قبلاً ثبت شده است.")
            return render(request, 'main/register.html')

        # ایجاد کاربر جدید
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name
        )

        # ایجاد پروفایل و ثبت شماره تلفن
        Profiles.objects.create(user=user, phone_number=phone_number)

        messages.success(request, "ثبت‌نام با موفقیت انجام شد. حالا وارد شوید.")
        return redirect('main/login')

    return render(request, 'main/register.html')
def intership_view(request):
    return render(request, 'intership.html')
def employer_view(request):
    return render(request, 'employer.html' )
def reg2_view(request):
    return render(request, 'reg2.html')


   

