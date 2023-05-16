from account.models import *
from .models import *
from django.forms import ModelForm


class HesapForm(ModelForm):
    class Meta:
        model= Hesap
        fields = ['isim' , 'soyisim' , 'bio' , 'resim']
        
    def __init__(self, *args , **kwargs):
        super(HesapForm , self).__init__(*args , **kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class' : 'form-control'})    

class PostForm(ModelForm):
    class Meta:
        model=Post
        fields =[
            'content' , 'resim'
        ]
    def __init__(self, *args , **kwargs):
        super(PostForm , self).__init__(*args , **kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class' : 'form-control'})   


class YorumForm(ModelForm):
    class Meta: 
        model = Yorum
        fields = [
            'yorum'
        ]
    def __init__(self,*args , **kwargs):
        super(YorumForm , self).__init__(*args , **kwargs)
        for name,fields in self.fields.items():
            fields.widget.attrs.update({'class' : 'form-control'})    