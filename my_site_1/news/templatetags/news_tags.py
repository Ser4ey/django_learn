from django import template

from news.models import Category

register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('news/list_categories.html')
def show_categories(active_category_pk='-1'):
    categories = Category.objects.all()
    return {'categories': categories, 'active_category_pk': active_category_pk}





