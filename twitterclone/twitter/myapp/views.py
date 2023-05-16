from django.shortcuts import render ,redirect ,get_object_or_404
from django.contrib.auth import authenticate
from django.contrib import messages
from .forms import *
from .models import *
import random




# Create your views here.
def begen(request):
        postId = request.POST['postId']
        post = Post.objects.get(id = postId)
        if 'begen' in request.POST:
            if Post.objects.filter(like__in = [request.user], id = postId).exists():
                post.like.remove(request.user)
                post.save()
                
            else:
                post.like.add(request.user)
                post.dislike.remove(request.user)
                post.save()
                

        if 'begenme' in request.POST:
            if Post.objects.filter(dislike__in = [request.user], id = postId).exists():
                post.dislike.remove(request.user)
                post.save()
                

            else:
                post.dislike.add(request.user)
                post.like.remove(request.user)
                post.save()
                

        if 'paylas' in request.POST:
            if Post.objects.filter(retweet__in = [request.user], id = postId).exists():
                post.retweet.remove(request.user)
                post.save()
                

            else:
                post.retweet.add(request.user)
                post.save()  
                

def kesfet(request):

    posts = Post.objects.all().order_by('?')
    profiller = Hesap.objects.exclude(takipci__in =[request.user.id]).order_by('?')


    form = PostForm()
    if 'tweet' in request.POST:
        form = PostForm(request.POST , request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            messages.success(request , 'Tweetledin')
            return redirect('anasayfa')
    if request.method == 'POST':
        begen(request)

    context ={
        'posts' : posts,
        'profiller' : profiller,
        'form' : form,

    }
    return render(request , 'kesfet.html' , context)

def anasayfa(request):

    defaults = [ 
        'image/sosyal.webp',
        'image/sosyal1.jpg',
        'image/sosyal2.jpg',
        'image/sosyal3.jfif',
        'image/sosyal4.jpg',
        'image/sosyal5.jpg',
    ]

    default = random.choice(defaults)

    
    posts = Post.objects.all()
    
    profiller = Hesap.objects.exclude(takipci__in =[request.user.id ]).order_by('?')
    profillerim = Hesap.objects.filter(takipci__in = [request.user.id]).order_by('?')

    form = PostForm()
    if 'tweet' in request.POST:
        form = PostForm(request.POST , request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            messages.success(request , 'Tweetledin')
            return redirect('anasayfa')
    if request.method == 'POST':
        begen(request)
        

    context = {
        'form' : form,
        'posts' : posts,
        'profiller' : profiller,
        'profillerim':profillerim,
        'default' :default
    }

    return render(request , "anasayfa.html",context)

def profil(request):
    user = request.user

    paylasim = Post.objects.filter(owner = request.user)
    begeni = Post.objects.filter(like__in = [request.user])
    retweet = Post.objects.filter(retweet__in = [request.user])

    # Profil düzenleme
    kullanici = request.user.hesap
    form = HesapForm(instance = kullanici)
    if 'profilduzenle' in request.POST:
        form = HesapForm(request.POST , request.FILES , instance = kullanici)
        if form.is_valid():
            form.save()
            messages.success(request , 'Profiliniz güncellendi')
            return redirect ('profile')
    
    # Şifre değiştirme  
    if 'sifredegis' in request.POST:
        eski = request.POST['eski']
        yeni1 = request.POST['yeni1']
        yeni2 = request.POST['yeni2']    

        yeni = authenticate(request, username = user , password = eski)
        if yeni is not None:
            if yeni1 == yeni2:
                user.set_password(yeni1)
                user.save()
                messages.success(request,'Şifreniz Değişti')
                return redirect('login')
            else:
                messages.error(request,'Şifreler uyuşmuyor')
                return redirect('profile')
        else:
            messages.error(request , 'Mevcut Şifreniz Hatalı')   
            return redirect('profile')     
    

    if request.method == 'POST':
        begen(request)
    context = {
        'user' : user,
        'form' : form,
        'paylasim' : paylasim,
        'begeni' : begeni ,
        'retweet' : retweet
        
    }
    return render(request , 'profile.html',context)

def userProfil(request , pk):
    user = User.objects.get(id = pk)

    paylasim = Post.objects.filter(owner = user)
    begeni = Post.objects.filter(like__in = [user])
    retweet = Post.objects.filter(retweet__in = [user])
    print(user.hesap)
    if request.method == 'POST':
        if 'takip' not in request.POST:
            begen(request)
            return redirect ('anasayfa')
        if 'takip' in request.POST:
            if request.user.is_authenticated:
                hesabim = Hesap.objects.get(user = request.user)
                if Hesap.objects.filter(user = request.user , takip__in = [user]).exists():
                    hesabim.takip.remove(user)
                    user.hesap.takipci.remove(request.user)
                    hesabim.save()
                    user.hesap.save()

                else: 
                    hesabim.takip.add(user)
                    user.hesap.takipci.add(request.user)
                    user.hesap.save()
                    hesabim.save()    
        return redirect('userProfil' , pk = user.id)

    context = {
        'user' : user ,
        'paylasim' : paylasim,
        'begeni' : begeni ,
        'retweet' : retweet,
     }
    
    return render(request , 'user-profile.html' , context)

def postDetay(request , pk):

    postdetay = Post.objects.get(id = pk)
    form = YorumForm()
    if 'yorumButton' in request.POST:
        form = YorumForm(request.POST or None)
        if form.is_valid():
            yorum = form.save(commit=False)
            yorum.post = postdetay
            yorum.kullanici = request.user
            yorum.save()
            return redirect('postDetay' , pk = postdetay.id)
    yorumlar = Yorum.objects.filter(post = postdetay)

    if 'sil' in request.POST:
        yorumId = request.POST['userYorum']
        yorum = Yorum.objects.get(id = yorumId)
        yorum.delete()
    


    context = {
        'postdetay' :postdetay,
        'form' : form,
        'yorumlar' : yorumlar
    }
    
    return render(request , 'post-detay.html' ,context)

def postDelete(request,pk):
    user = request.user.hesap

    post = Post.objects.get(id = pk)
    post.delete()

    return redirect('profile')

def search(request):

    kullanicilar = ''
    searched = ''

    if request.GET.get('searched'):
        searched = request.GET['searched']
        kullanicilar = Hesap.objects.filter(
            isim__contains = searched
        )
    context = {
        'kullanicilar' : kullanicilar
    }

    return render (request , 'search.html',context)


def takipedilecek(request):
    profiller = Hesap.objects.exclude(takipci__in =[request.user.id]).order_by('?')

    context = {
        'profiller' : profiller

    }
    

    return render(request , 'takipedilecek.html',context)