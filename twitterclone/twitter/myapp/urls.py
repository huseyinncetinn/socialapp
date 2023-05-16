from django.urls import path
from . import views


urlpatterns = [
    path('', views.anasayfa , name='anasayfa'),
    path('profile/' , views.profil , name='profile'),
    path('other/<str:pk>' , views.userProfil , name='userProfil'),
    path('postdetay/<str:pk>', views.postDetay , name='postDetay'),
    path('kesfet/' , views.kesfet , name='kesfet'),
    path('deletePost/<str:pk>' , views.postDelete , name='deletePost'),
    path('search/' , views.search , name='search'),
    path('takipönerisi/' , views.takipedilecek , name='takipedilecek')
  
]
