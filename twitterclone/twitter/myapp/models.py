from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.

class Post(models.Model):
    id = models.UUIDField(primary_key=True,db_index=True , default=uuid.uuid4 , editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=150)
    resim = models.FileField(upload_to = 'postlar/',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(User , related_name='like')
    dislike = models.ManyToManyField(User , related_name='dislike')
    retweet = models.ManyToManyField(User, related_name='retweet')

    def __str__(self):
        return self.owner.username

class Yorum(models.Model):
    id = models.UUIDField(primary_key=True , db_index=True , default=uuid.uuid4 , editable=False)
    post = models.ForeignKey(Post,related_name='yorum' , on_delete=models.CASCADE)
    yorum = models.TextField(max_length=50 , verbose_name='yorum')
    yorumTarih = models.DateTimeField(auto_now_add=True)
    kullanici = models.ForeignKey(User, null=True , on_delete=models.CASCADE)

    def __str__(self):
        return str(self.post.owner)
    
