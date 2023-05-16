from django.shortcuts import render,redirect
from django.contrib.auth import authenticate , logout
from django.contrib.auth.models import User
from account.models import *
from django.contrib import messages
from django.contrib.auth import login as auth_login

# Create your views here.

def login(request):

    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request , username = username , password = password)
        if user is not None :
            auth_login(request , user)
            messages.success(request , 'Giriş yapıldı')
            return redirect("anasayfa")
        else:
            messages.error(request , 'Kullanıcı adı veya şifre yanlış')
            return render(request,"login.html")

    return render(request , "login.html")


def userRegister(request):
    
    if request.method == "POST":
        kullanici = request.POST["kullanici"]
        email = request.POST["email"]
        isim = request.POST["isim"]
        soyisim = request.POST["soyisim"]
        sifre1 = request.POST["sifre1"]
        sifre2 = request.POST["sifre2"]

        if sifre1 ==  sifre2 :
            if User.objects.filter(username = isim).exists():
                messages.error(request,'Kullanıcı adı kullanılıyor')
                return redirect("register")
            elif User.objects.filter(email = email).exists():
                messages.error(request,'Email kullanılıyor')
                return redirect("register")
            elif len(sifre1) < 6 :
                messages.error(request , 'Şifre en az 6 karakter olmalıdır')
                return redirect("register")
            else:
                user = User.objects.create_user(username = kullanici , email = email , password = sifre1 )
                Hesap.objects.create(
                    user = user ,
                    isim = isim , 
                    soyisim = soyisim
                )
                user.save()
                messages.success(request,'Kayıt başarı ile gerçekleşti')
                return redirect("login")
        else :
            messages.error(request,'Şifreler uyuşmuyor')
            return render(request , "register.html")

    
    return render(request , "register.html")
    
def logout_request(request):
    logout(request)
    return redirect ("anasayfa")