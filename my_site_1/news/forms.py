from django import forms
from .models import Category


class NewsForm(forms.Form):
    title = forms.CharField(max_length=150, label='Заголовок новости:',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Контент:', required=False)
    is_published = forms.BooleanField(label='Опубликовано:', initial=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      label='Категория:',
                                      empty_label='Выберите категорию')












