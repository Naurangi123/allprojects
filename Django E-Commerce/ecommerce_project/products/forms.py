from .models import Product,Category,Review
from django import forms


class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = '__all__'        
        
class CategaryFrom(forms.ModelForm):
    cat_name=forms.CharField()
    
    class Meta:
        model = Category
        fields=['cat_name']
        

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.TextInput(),
        }