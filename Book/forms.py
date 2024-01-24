from django import forms
from .models import Book

class BookCreate(forms.ModelForm):
    
    class meta:
        model = Book
        fields = '__all__'
            