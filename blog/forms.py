from django import forms
from .models import Article


class ArticleAddForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'body',)

