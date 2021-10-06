from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import News, Category
from .forms import NewsForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Вы успешно зарегистрировались!')
            form.save()
            return redirect('login')
        else:
            messages.error(request, 'Ошибка вилидации!')
    else:
        form = UserCreationForm()
    return render(request, 'news/register.html', {'form': form})


def login(request):
    return render(request, 'news/login.html', {'news': 'news'})


class HomeNews(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 2


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main page'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')
        # return News.objects.filter(is_published=True)


class NewsByCategory(ListView):
    model = News
    template_name = 'news/category.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(pk=self.kwargs['category_id'])
        print(context['category'])
        return context

    def get_queryset(self):
        # return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'
    template_name = 'news/view_news.html'


class CreateNews(LoginRequiredMixin, CreateView):
    # переадресация
    # login_url = '/admin/'

    # error 403
    raise_exception = True

    form_class = NewsForm
    template_name = 'news/add_news.html'


# def index(request):
#     news = News.objects.all()
#
#     context = {
#             'news': news,
#             'title': 'Список статей',
#     }
#
#     return render(request=request, template_name='news/index.html', context=context)


# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#
#     context = {
#         'news': news,
#         'category': category,
#     }
#
#     return render(request=request, template_name='news/category.html', context=context)


# def view_news(request, news_id):
#     # news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk=news_id)
#
#     context = {
#         'news_item': news_item,
#     }
#
#     return render(request=request, template_name='news/view_news.html', context=context)


# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             news1 = form.save()
#             return redirect(news1)
#     else:
#         form = NewsForm()
#     return render(request=request, template_name='news/add_news.html', context={'form': form})










