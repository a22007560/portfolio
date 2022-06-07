from django import forms
from django.forms import ModelForm
from .models import Blog


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
    # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Autor...'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo do Post...'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descrição do Post...'}),
        }


    # texto a exibir junto à janela de inserção
        labels = {
            'titulo': 'Título',
        }


    # texto auxiliar a um determinado campo do formulário
        help_texts = {
        }