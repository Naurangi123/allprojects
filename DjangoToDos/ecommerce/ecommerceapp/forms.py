from django import forms
 
from .models import UserProfile,Product



class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model=UserProfile
        fields="__all__"
        
        
class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields="__all__"