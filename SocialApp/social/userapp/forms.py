from django import forms

from .models import Post,MessageModel

class PostForm(forms.ModelForm):
    body = forms.CharField(label="", widget=forms.Textarea(attrs={'rows': '2', 'placeholder': 'Post Something...'}))
    
    image = forms.ImageField(required=False)
    
    class Meta:
        model = Post
        fields = ['body', 'image']


class ThreadForm(forms.Form):
    username = forms.CharField(label="", max_length=300)


class MessageForm(forms.ModelForm):
    body = forms.CharField(label="", max_length=300)
    image = forms.ImageField(required=False)
    
    class Meta:
        model = MessageModel
        
        fields = ['body', 'image']