from django import forms
from .models import News
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if title[0] in '0123456789':
            raise ValidationError('Название статьи не должно начинаться с цифры!')
        return title



# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=150, label='Заголовок новости:',
#                             widget=forms.TextInput(attrs={'class': 'form-control'}))
#     content = forms.CharField(label='Контент:', required=False,
#                               widget=forms.Textarea(attrs={
#                                   'class': 'form-control',
#                                   'rows': 5
#                               }))
#     is_published = forms.BooleanField(label='Опубликовано:', initial=True)
#
#     category = forms.ModelChoiceField(queryset=Category.objects.all(),
#                                       label='Категория:',
#                                       empty_label='Выберите категорию',
#                                       widget=forms.Select(attrs={'class': 'form-control'}))












