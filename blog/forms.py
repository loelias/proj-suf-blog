from django import forms

from .models import Post, Comentario


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('titulo', 'texto',)
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite um Título'}),
            'texto': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ('autor', 'texto',)
        widgets = {
            'autor': forms.EmailInput(attrs={
                'class': 'form-control', 'placeholder': 'Digite seu email'}),
            'texto': forms.TextInput(attrs={'class': 'form-control'}),
        }
